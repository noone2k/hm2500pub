// Datenpunkte-Definitionen mit Namen auf Deutsch
itemLabels = {
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
};


//edit BELOW
var itemParent = "B2500V2__MQTT__intern";
var itemGroup  = "B2500V2__MQTT__intern_B2500V2__MQTT__1__";
var itemLabel  = "B2500V2 - MQTT - 1 - DATA";
//edit END

var itemGroupSUB = itemGroup + "SUB";
var itemGroupDATA = itemGroup + "DATA";

//check for GroupData and add if not exists
if (items.getItem(itemGroupDATA, true) == null) {
  //console.log("Group not found: " + itemGroupDATA);
  items.addItem({name: itemGroupDATA, type: 'Group', label: itemLabel, groups: [itemParent], tags: ['Equipment']});
}

// edit NEXT Line
var data = items.B2500V2__MQTT__intern_B2500V2__MQTT__1__SUB.state;

//var data = items.${itemGroupSUB}.state;
var values = data.split(',');

// gesamtleistung ein- und ausgange
var w3 = 0;
var g3 = 0;

values.forEach((value) => {
  const [key, val] = value.split('=');
  //console.log(key + ": " + val);
  
  var itemName = itemGroupDATA + "_" + key;
  var item = items.getItem(itemName, true);

  // create/update items
  if (item == null) {
    //console.log("Item not found: " + itemName + "(" + itemLabels[key] + ")");
    var itemType = "Number"
    if (key === "e1" || key === "f1" || key === "e2" || key === "f2" || key === "e3" || key === "f3" ) { itemType = "String"; }
    items.addItem({name: itemName, type: itemType, label: itemLabels[key], groups: [itemGroupDATA], tags: ['Point']});
  } else {
    item.postUpdate(val);
  }
  
  // gesamtleistung ein- und ausgange
  if ( key === "w1" || key === "w2") { w3 += Number(val); }
  if ( key === "g1" || key === "g2") { g3 += Number(val); }

})

// additional/calculated values
// gesamtleistung eingang
var key = "w3";
var itemName = itemGroupDATA + "_" + key;
var item = items.getItem(itemName, true);
if (item == null) {
  items.addItem({name: itemName, type: 'Number', label: itemLabels[key], groups: [itemGroupDATA], tags: ['Point']});
} else {
  item.postUpdate(w3);
}
// gesamtleistung ausgang
var key = "g3"
var itemName = itemGroupDATA + "_" + key;
var item = items.getItem(itemName, true);
if (item == null) {
  items.addItem({name: itemName, type: 'Number', label: itemLabels[key], groups: [itemGroupDATA], tags: ['Point']});
} else {
  item.postUpdate(g3);
}
// gesamtleistung eingang
var key = "last";
var timestamp = time.ZonedDateTime.now().format(time.DateTimeFormatter.ofPattern('dd.MM.yyyy HH:mm:ss'));
//console.log("Timestamp: " + timestamp);
var itemName = itemGroupDATA + "_" + key;
var item = items.getItem(itemName, true);
if (item == null) {
  items.addItem({name: itemName, type: 'String', label: itemLabels[key], groups: [itemGroupDATA], tags: ['Point']});
} else {
  item.postUpdate(timestamp);
}

