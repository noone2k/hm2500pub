# openhab example script

Dieses inline script für rules
parsed und erstellt die Items im Model für die per MQTT ausgelesenen Werte.

damit das ganze funktionmiert muss ein THING erstellt werden, mit dem SUB und
zwei rules.
in dem THING kann man der einfachheithalber ein PUB einrichten,
um später auch Befehle über das gleiche THING zu senden.


 1. eine rule für den publish
    topic: hame_energy/$DEV_TYPE/App/$DEV_MAC/ctrl
    cmd: cd=01
    bspw. mit nem script, das alle 5 sekunden den befehl sendet.

    - ab fw 216 ( und 141* ), cd=13* / cd=14 / cd=15* / cd=16* / cd=21* / cd=24

 3. die zweite sollte auf das item reagieren, wo die antwort landet, von der ersten rule.
    als inline script für die 2 rule, kann man das hier hinterlegte als vorlage nehmen.
    muss natürlich an eurer system angepasst werden.


more infos to come ... maybe :)
