#!/bin/bash

# --- CONFIGURATION ---
HOST="192.168.XX.XXX"

DEV_TYPE="HMJ-2"
DEV_MAC="XXXXXXXXXXXX"

TOPIC_PUB="hame_energy/$DEV_TYPE/App/$DEV_MAC/ctrl"
TOPIC_SUB="hame_energy/$DEV_TYPE/device/$DEV_MAC/ctrl"
MSG="cd=30"

MAX_ATTEMPTS=5
RAW_INPUT=""

# Fehlercodes Dictionary (Dezimal-Keys)
declare -A shorts_diz
shorts_diz[0]="Device startup"
shorts_diz[12]="Battery Overvoltage"
shorts_diz[25]="Watchdog reset"
shorts_diz[33]="Lithium short circuit protection"
shorts_diz[35]="Single battery overvoltage"
shorts_diz[36]="Single section undervoltage"
shorts_diz[42]="Register notification undervoltage"
shorts_diz[43]="Under voltage condition enters sleep mode"
shorts_diz[55]="Start discharge learning"
shorts_diz[56]="Start charging and learning"
shorts_diz[57]="Interrupted discharge learning"
shorts_diz[61]="Charging learning completed"
shorts_diz[62]="Invalid learning data"
shorts_diz[63]="Discharge opens and exits charging learning"
shorts_diz[64]="Enter warehouse transportation mode"
shorts_diz[65]="Wake up in warehouse transportation mode"
shorts_diz[74]="MQTT open failed"
shorts_diz[75]="MQTT connection disconnected"
shorts_diz[76]="MQTT reconnect"
shorts_diz[77]="DOD stops discharging"
shorts_diz[78]="MQTT connection successful"
shorts_diz[79]="MQTT connection error / Bind monitor IP"
shorts_diz[80]="MQTT re upload"
shorts_diz[81]="MQTT certificate deletion"
shorts_diz[82]="MQTT upload successful"
shorts_diz[84]="Output 1 abnormal / HTTPGET error"
shorts_diz[85]="Output 2 abnormal"
shorts_diz[86]="HTTP POST error"
shorts_diz[87]="battery pack DOD parking"
shorts_diz[88]="Battery Pack Switching"
shorts_diz[89]="Output 1 channel abnormal"
shorts_diz[90]="Battery pack comms abnormality / Output 2 channel abnormal"
shorts_diz[91]="Device restart / HTTPPOST error"
shorts_diz[92]="Battery pack DOD parking / Operator 309 MOS"
shorts_diz[94]="Battery pack switching"
shorts_diz[100]="Risk of backflow"

# Temporäre Log-Datei für den Hintergrund-Prozess erstellen
TMP_LOG=$(mktemp)

# Funktion zum Aufräumen bei Skriptende
cleanup() {
    kill "$SUB_PID" 2>/dev/null
    rm -f "$TMP_LOG"
}
trap cleanup EXIT

echo "Starte Abfrage-Stream..."
echo "--------------------------------------------------------------------------------"

# 1. MQTT-Subscriber startet im Hintergrund und schreibt JEDES Zeichen SOFORT ins File
# Das Flag "-N" sorgt dafür, dass Daten nicht auf einen Zeilenumbruch warten müssen
mosquitto_sub -h "$HOST" -t "$TOPIC_SUB" -N >> "$TMP_LOG" &
SUB_PID=$!

# Kurze Pause, damit der Subscriber sicher verbunden ist
sleep 0.5

# 2. Sende- und Überwachungsschleife
for (( attempt=1; attempt<=MAX_ATTEMPTS; attempt++ )); do
    echo "[Versuch $attempt/$MAX_ATTEMPTS] Sende Befehl '$MSG'..."
    mosquitto_pub -h "$HOST" -t "$TOPIC_PUB" -m "$MSG"

    # Wir prüfen in den nächsten 5 Sekunden sekündlich, was im Log steht
    for (( check=1; check<=5; check++ )); do
        sleep 1
        
        # Inhalt der Datei auslesen und Leerzeichen entfernen
        CURRENT_CONTENT=$(tr -d '[:space:]' < "$TMP_LOG")

        # Wenn der String extrem lang ist, ist das unser Log-Paket!
        if [ ${#CURRENT_CONTENT} -gt 20 ]; then
            # Wir suchen das Ende der bekannten "Busy-Meldungen" (z.B. 01ff, 02ff, 0ff0)
            # Und schneiden das eigentliche Log heraus.
            # Da das Log numerisch beginnen soll, filtern wir Dreck am Anfang weg.
            if [[ "$CURRENT_CONTENT" =~ (00[0-9a-fA-F]{20,}) || "$CURRENT_CONTENT" =~ ([0-9a-fA-F]{20,}) ]]; then
                RAW_INPUT="${BASH_REMATCH[0]}"
                echo "   => Valides Log erkannt (${#RAW_INPUT} Zeichen)!"
                break 2 # Bricht sowohl die Check- als auch die Hauptschleife ab
            fi
        elif [ -n "$CURRENT_CONTENT" ]; then
            echo "   -> Status vom Gerät im Puffer: '$CURRENT_CONTENT'"
        fi
    done
    
    # Falls nach 5 Sekunden kein langes Log da war, leeren wir den Puffer für die nächste Runde
    > "$TMP_LOG"
done

# Subscriber beenden
cleanup

# Prüfen, ob Daten isoliert werden konnten
if [ -z "$RAW_INPUT" ]; then
    echo "--------------------------------------------------------------------------------"
    echo "Fehler: Auch im 4./5. Versuch wurde kein langes Log-Paket isoliert."
    exit 1
fi

# --- PARSER LOGIC ---
echo "--------------------------------------------------------------------------------"
echo "Verarbeite empfangene Daten..."
echo "--------------------------------------------------------------------------------"

# Erstes Byte '00' weglassen
INPUT="${RAW_INPUT:2}"
BLOCK_SIZE=18

for (( i=0; i<${#INPUT}; i+=BLOCK_SIZE )); do
    BLOCK="${INPUT:i:BLOCK_SIZE}"
    
    if [ ${#BLOCK} -ne $BLOCK_SIZE ]; then
        echo "--> Unvollständiger Block am Ende ignoriert: $BLOCK"
        break
    fi

    ERR_HEX="${BLOCK:0:2}"
    EPOCH_HEX="${BLOCK:2:8}"
    DATA_HEX="${BLOCK:10:8}"

    ERR_DEC=$((16#$ERR_HEX))
    EPOCH_DEC=$((16#$EPOCH_HEX))
    DATA_DEC=$((16#$DATA_HEX))
    
    DATE_HUMAN=$(date -d "@$EPOCH_DEC" "+%Y-%m-%d %H:%M:%S" 2>/dev/null || echo "Ungültiges Datum")

    ERROR_DESC="${shorts_diz[$ERR_DEC]}"
    if [ -z "$ERROR_DESC" ]; then
        ERROR_DESC="Unbekannter Fehlercode"
    fi

    echo "Raw: $BLOCK"
    echo "  ├─ Event/Error: $ERR_DEC (0x$ERR_HEX) -> $ERROR_DESC"
    echo "  ├─ Zeitstempel: $DATE_HUMAN ($EPOCH_DEC)"
    echo "  └─ Zusatz-Data: $DATA_DEC (0x$DATA_HEX)"
    echo "--------------------------------------------------------------------------------"
done

