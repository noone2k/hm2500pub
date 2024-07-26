# home assistent example script

dieses python_script parsed the antwort und splitted diese auf.
hier fehlt jetzt nur noch das update/create der entities.

sollte den einstieg aber erleichtern.

vorraussetzung:
HA mit aktivierten python_script und wenn man zum testen loggen will,
mit aktivierten logger ( in der configuration.yaml ) :

```
python_script:

logger:
  default: info
```

es werden auch bei diesem ansatz erstmal zwei automationen benötigt.
einen zum senden des befehl sowie zum ausführen des parser scripts bei der antwort.


example log:

```
2024-07-27 00:03:21.803 INFO (SyncWorker_6) [homeassistant.components.python_script] Executing b2500_parse_respond.py: {'message': 'p1=0,p2=0,w1=0,w2=0,pe=75,vv=139,cs=1,cd=3,am=0,o1=1,o2=1,do=90,lv=999,cj=1,kn=3337,g1=38,g2=38,b1=1,b2=0,tl=25,th=26,tc=0,tf=0,fc=202310231502'}
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] p1 - Solar-Eingangsstatus 1 : 0
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] p2 - Solar-Eingangsstatus 2 : 0
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] w1 - Solar-Eingangsleistung 1 : 0
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] w2 - Solar-Eingangsleistung 2 : 0
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] pe - Batterieprozentsatz : 75
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] vv - Geräteversionsnummer : 139
2024-07-27 00:03:21.804 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] cs - Ladeeinstellungen : 1
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] cd - Entladeeinstellungen : 3
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] am - AM : 0
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] o1 - Ausgangszustand 1 : 1
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] o2 - Ausgangszustand 2 : 1
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] do - Entladetiefe (DoD) : 90
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] lv - Batterieentladeschwelle : 999
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] cj - Szene : 1
2024-07-27 00:03:21.805 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] kn - Batteriekapazität : 3337
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] g1 - Ausgangsleistung 1 : 38
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] g2 - Ausgangsleistung 2 : 38
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] b1 - Ist Power Pack 1 verbunden : 1
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] b2 - Ist Power Pack 2 verbunden : 0
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] tl - Mindesttemperatur der Batteriezellen : 25
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] th - Höchsttemperatur der Batteriezellen : 26
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] tc - Ladetemperaturalarm : 0
2024-07-27 00:03:21.806 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] tf - Entladetemperaturalarm : 0
2024-07-27 00:03:21.807 INFO (SyncWorker_6) [homeassistant.components.python_script.b2500_parse_respond.py] fc - Chip FC4 Versionsnummer : 202310231502
```
