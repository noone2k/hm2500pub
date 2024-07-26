message = data.get("message")

# short_diz
shortDiz = {
"p1": "Solar-Eingangsstatus 1",
"p2": "Solar-Eingangsstatus 2",
"w1": "Solar-Eingangsleistung 1",
"w2": "Solar-Eingangsleistung 2",
"pe": "Batterieprozentsatz",
"vv": "Geräteversionsnummer",
"cs": "Ladeeinstellungen",
"cd": "Entladeeinstellungen",
"am": "AM",
"o1": "Ausgangszustand 1",
"o2": "Ausgangszustand 2",
"do": "Entladetiefe (DoD)",
"lv": "Batterieentladeschwelle",
"cj": "Szene",
"kn": "Batteriekapazität",
"g1": "Ausgangsleistung 1",
"g2": "Ausgangsleistung 2",
"b1": "Ist Power Pack 1 verbunden",
"b2": "Ist Power Pack 2 verbunden",
"md": "Entlademodus-Einstellung",
"d1": "Zeit 1 Aktivierungsstatus",
"e1": "Zeit 1 Startzeit",
"f1": "Zeit 1 Endzeit",
"h1": "Zeit 1 Ausgangswert",
"d2": "Zeit 2 Aktivierungsstatus",
"e2": "Zeit 2 Startzeit",
"f2": "Zeit 2 Endzeit",
"h2": "Zeit 2 Ausgangswert",
"d3": "Zeit 3 Aktivierungsstatus",
"e3": "Zeit 3 Startzeit",
"f3": "Zeit 3 Endzeit",
"h3": "Zeit 3 Ausgangswert",
"sg": "Ist der Sensor verbunden",
"sp": "Automatische Leistungsgröße des Monitors",
"st": "Vom Monitor übertragene Leistung",
"tl": "Mindesttemperatur der Batteriezellen",
"th": "Höchsttemperatur der Batteriezellen",
"tc": "Ladetemperaturalarm",
"tf": "Entladetemperaturalarm",
"ts": "WiFi-Signalerkennung",
"fc": "Chip FC4 Versionsnummer",
"id": "ID",
"a0": "A0",
"a1": "A1",
"a2": "A2",
"l0": "L0",
"l1": "L1",
"sv": "SV",
"w3": "Solar Gesamt",
"g3": "Ausgangsleistung gesamt",
"last": "Timestamp"
}



# create dict from message
b2500_dict = {}
val_keys = message.split(",")
for vk in val_keys:
    x = vk.split("=")
    b2500_dict[x[0]] = x[1]

# log output - only for testing
for x in b2500_dict:
    logger.info("{} - {} : {}".format(x , shortDiz[x], b2500_dict[x]))

# hass.states.set(entity_id, 'state', attributes)
