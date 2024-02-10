# hm2500pub

- config options ( secret.yaml )
    ( max 2. hm2500 )
    * hm2500_1_mac: "E8:8D:A6:XX:XX:XX"
    * hm2500_2_mac: "E8:8D:A6:XX:XX:XX"

    ( powerzero )
    * mqtt_grid_power: "tibber-esp/sensor/power/state"
    * mqtt_opendtu_limit_state: "openDTU/XXXXXXXXXXXX/state/limit_relative"
    * mqtt_opendtu_limit_cmd: "openDTU/XXXXXXXXXXXX/cmd/limit_persistent_relative"


- common errors:
 * Source `XXXXXXX' not found, needed by target
    changed components: esphome clean config/bc2500-*.yaml

 * collect2: error: ld returned 1 exit status
    changed components: esphome clean config/bc2500-*.yaml

 * ble / wifi connectect error/failed
    try to erase whole flash: esptool.py erase_all



- HA-Version ( npw2500 ) by neromatrix
 * https://gist.github.com/neromatrix/6ec812f35418c4b38ebbad4e92cac888


