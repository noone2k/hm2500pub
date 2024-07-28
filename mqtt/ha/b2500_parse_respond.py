message = data.get("message")
topic = data.get("topic")

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
"last": "Timestamp",
"type": "Geräte-Type",
"mac": "BLE Mac"
}

valunits = {
"w1": "W",
"w2": "W",
"w3": "W",
"g1": "W",
"g2": "W",
"g3": "W",
"pe": "%",
"kn": "kWh",
"tl": "°C",
"th": "°C",
"do": "%",
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
    #logger.info("itemX: {} - diz: {} - value: {}".format(itemX , shortDiz[itemX], value))

    if itemX == "o1" or itemX == "o2" or itemX == "b1" or itemX == "b2" or itemX == "p1" or itemX == "p2":
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
        inputAttributesObject["friendly_name"] = shortDiz[x]
        inputAttributesObject["unique_id"] = inputEntity
        if x in valunits:
            inputAttributesObject["unit_of_measurement"] = valunits[x]

    hass.states.set(inputEntity, value, inputAttributesObject)


# update/create items
for x in b2500_dict:
    #logger.info("{} - {} : {}".format(x , shortDiz[x], b2500_dict[x]))
    items_update(x,b2500_dict[x])

