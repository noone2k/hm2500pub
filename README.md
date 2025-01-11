# hm2500pub

HW Version 1 ( HMB-X ) :  bc2500-ble-idf.yaml

HW Version 2 ( HMA-X ) :  b2500-v2-ble-idf.yaml

----------------------

- only some notes ... vllt. wirds ja mal ne ordentlich readme :D

- config options ( secret.yaml )
    ( max 2. hm2500 - HMB-X )
    * hm2500_1_mac: "E8:8D:A6:XX:XX:XX"
    * hm2500_2_mac: "E8:8D:A6:XX:XX:XX"

    ( max 2. hm2500 - HMA-X )
    * hm2500_3_mac: "E8:8D:A6:XX:XX:XX"
    * hm2500_4_mac: "E8:8D:A6:XX:XX:XX"


-  powerzero nur in v1
    * mqtt_grid_power: "tibber-esp/sensor/power/state"
    * mqtt_opendtu_limit_state: "openDTU/XXXXXXXXXXXX/state/limit_relative"
    * mqtt_opendtu_limit_cmd: "openDTU/XXXXXXXXXXXX/cmd/limit_nonpersistent_relative"

- Webinterface ( im Prinzip läuft das dann standalone - momentan nur v1 ):
    A(X) -- Informationen zum Gerät ( X = 1/2 , entspricht Batterie 1 oder 2 )
    D(X) -- Status Informationen

    Enhanced - Erweiterte Einstellungen/Optionen, die durch die ESP ausgeführt werden-
                ( kontinuierlich BT erfordlerlich !!!! )

        * Enforce DOD - schaltet beim erreichen des DOD die Ausgänge aus
        * enable Cell Query (cmd0F) - erfragt die Zellspannungen alle 10Sekunden
        * enable unknown Query (cmd30) - sendet cmd 0x30 ... 1 Minute
        ------ todo ??? ------
        * ??????? DOD - einschalten der Ausgänge beim Erreichen von XX Prozent
        * Enforce Safe Settings - PV1/PV2/PV2Passthrough off / DOD 80 / etc. 
        * Enforce Custom Settings - custom ^^
        bei neustart des ESP32 und/oder bei einer neuen BT Verbindung ( bspw. u.a. nach nem reset )
        ----------------------

    MQTT - ZeroPower Einstellungen von neromatrix ( MQTT only Adapation )

- MQTT:
    Die meisten Sensoren, Einstellungen können auch per MQTT eingesehen/geregelt werden.
    * b2500/(X)/.....
        
- common errors:
 * Source `XXXXXXX' not found, needed by target
    changed components: esphome clean config/bc2500-*.yaml

 * collect2: error: ld returned 1 exit status
    changed components: esphome clean config/bc2500-*.yaml

 * ble / wifi connectect error/failed
    try to erase whole flash: esptool.py erase_all

**3rd party links/tools/helpers/etc. **

- HA-Version for V1 ( npw2500 ) by neromatrix
  * https://gist.github.com/neromatrix/6ec812f35418c4b38ebbad4e92cac888

- Online Generator for YAML by tomquist ( upto 3 devices )
  * https://tomquist.github.io/esphome-b2500/

- Smartmeter Emulator by tomquist
  * https://github.com/tomquist/b2500-meter

- FreeYourGadget / Java Implementation
   * https://codeberg.org/Freeyourgadget/Gadgetbridge/src/branch/master/app/src/main/java/nodomain/freeyourgadget/gadgetbridge/service/devices/marstek/MarstekB2500DeviceSupport.java

