message = data.get("message")
topic = data.get("topic")

# short : [ diz, class, unit ]
entityDiz = {
        "p1": [ "Solar-Eingangsstatus 1", "power", None ],
        "p2": [ "Solar-Eingangsstatus 2", "power", None ],
        "w1": [ "Solar-Eingangsleistung 1", "power", "W" ],
        "w2": [ "Solar-Eingangsleistung 2", "power", "W" ],
        "pe": [ "Batterieprozentsatz", "battery", "%" ],
        "vv": [ "Geräteversionsnummer", None, None ],
        "cs": [ "Ladeeinstellungen", None, None ],
        "cd": [ "Entladeeinstellungen", None, None ],
        "am": [ "AM", None, None ],
        "o1": [ "Ausgangszustand 1", "power", None ],
        "o2": [ "Ausgangszustand 2", "power", None ],
        "do": [ "Entladetiefe (DoD)", None, "%" ],
        "lv": [ "Batterieentladeschwelle", None, None ],
        "cj": [ "Szene", None, None ],
        "kn": [ "Batteriekapazität", "energy", "kWh" ],
        "g1": [ "Ausgangsleistung 1", "power", "W" ],
        "g2": [ "Ausgangsleistung 2", "power", "W" ],
        "b1": [ "Power Pack 1 verbunden", "power", None ],
        "b2": [ "Power Pack 2 verbunden", "power", None ],
        "md": [ "Entlademodus-Einstellung", None, None ],
        "d1": [ "Zeit 1 Aktivierungsstatus", None, None ],
        "e1": [ "Zeit 1 Startzeit", None, None ],
        "f1": [ "Zeit 1 Endzeit", None, None ],
        "h1": [ "Zeit 1 Ausgangswert", "power", "W" ],
        "d2": [ "Zeit 2 Aktivierungsstatus", None, None ],
        "e2": [ "Zeit 2 Startzeit", None, None ],
        "f2": [ "Zeit 2 Endzeit", None, None ],
        "h2": [ "Zeit 2 Ausgangswert", "power", "W" ],
        "d3": [ "Zeit 3 Aktivierungsstatus", None, None ],
        "e3": [ "Zeit 3 Startzeit", None, None ],
        "f3": [ "Zeit 3 Endzeit", None, None ],
        "h3": [ "Zeit 3 Ausgangswert", "power", "W" ],
        "sg": [ "Monitor verbunden", None, None ],
        "sp": [ "Monitor Ausgangsleistung",  "power", "W" ],
        "st": [ "Monitor gemessene Leistung", "power" ,"W" ],
        "tl": [ "Mindesttemperatur der Batteriezellen",  "temperatur", "°C" ],
        "th": [ "Höchsttemperatur der Batteriezellen",  "temperatur", "°C" ],
        "tc": [ "Ladetemperaturalarm",  None, None ],
        "tf": [ "Entladetemperaturalarm", None, None ],
        "ts": [ "WiFi-Signalerkennung", None, None ],
        "fc": [ "Chip FC4 Versionsnummer", None, None ],
        "id": [ "ID", None, None ],
        "a0": [ "Kapazität intern", "battery", "%" ],
        "a1": [ "Kapazität Powerpack 1", "battery","%" ],
        "a2": [ "Kapazität Powerpack 2", "battery","%" ],
        "l0": [ "L0", None, None ],
        "l1": [ "L1", None, None ],
        "sv": [ "SV", None, None ],
        "w3": [ "Solar Gesamt", "power", "W" ],
        "g3": [ "Ausgangsleistung gesamt", "power", "W" ],
        "last": [ "Timestamp", None, None ],
        "type": [ "Geräte-Typ", None, None ],
        "mac": [ "BLE Mac", None, None ],
}

# extract type and mac from topic
dev_type_mac = topic.split("/")
dev_type = dev_type_mac[1]
dev_mac = dev_type_mac[3]

# create dict from message/topic
b2500_dict = {}
val_keys = message.split(",")
for vk in val_keys:
    x = vk.split("=")
    b2500_dict[x[0]] = x[1]
# add type and mac to dict
b2500_dict["type"] = dev_type
b2500_dict["mac"] = dev_mac
# calc and add w3 / g3
b2500_dict["w3"] = int(b2500_dict["w1"]) + int(b2500_dict["w2"])
b2500_dict["g3"] = int(b2500_dict["g1"]) + int(b2500_dict["g2"])


# function to create/update items
def items_update(itemX,value):
#    logger.info("itemX: {} - diz: {} - value: {}".format(itemX , shortDiz[itemX], value))

    if itemX == "o1" or itemX=="o2" or itemX=="b1" or itemX=="b2" or itemX=="p1" or itemX=="p2" or itemX=="sg" or itemX=="d1" or itemX=="d2" or itemX=="d3":
        inputEntity = "binary_sensor.b2500_" + dev_mac + "_" + itemX
    else:
        inputEntity = "sensor.b2500_" + dev_mac + "_" + itemX

    inputStateObject = hass.states.get(inputEntity)
    if not inputStateObject is None:
        inputState = inputStateObject.state
        inputAttributesObject = inputStateObject.attributes.copy()
        if inputAttributesObject["state"] != value:
            inputAttributesObject["state"] = value
    else:
        logger.info("inputEntity: {} - : not found - create".format(inputEntity))
        inputState = value
        inputAttributesObject = {}
        inputAttributesObject["state"] = value
        inputAttributesObject["unique_id"] = inputEntity # doesnt work this way ... still keep it

        if itemX in entityDiz:
            inputAttributesObject["friendly_name"] = entityDiz[itemX][0]
            if not entityDiz[itemX][1] is None:
                inputAttributesObject["device_class"] = entityDiz[itemX][1]
            if not entityDiz[itemX][2] is None:
                inputAttributesObject["unit_of_measurement"] = entityDiz[itemX][2]

    hass.states.set(inputEntity, value, inputAttributesObject)


# update/create items
for x in b2500_dict:
    #logger.info("{} - {} : {}".format(x , shortDiz[x], b2500_dict[x]))
    items_update(x,b2500_dict[x])

