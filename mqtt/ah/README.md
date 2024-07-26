# home assistent example script

dieses python_script parsed the antwort und splitted diese auf.
hier fehlt jetzt nur noch das update/create der entities.

sollte den einstieg aber erleichtern.

vorraussetzung:
HA mit aktivierten python_script und wenn man zum testen loggen will,
mit aktivierten logger ( in der configuration.yaml ) :


python_script:

logger:
  default: info


es werden auch bei diesem ansatz erstmal zwei automationen benötigt.
einen zum senden des befehl sowie zum ausführen des parser scripts bei der antwort.

