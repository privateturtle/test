# -*- coding: utf-8 -*-
 
# importiert das json-Modul
import json

# Daten mit dicts und lists erfassen
daten = dict()
daten["herausgeber"] = "Xema"
daten["Nummer"] = "1234-5678-9012-3456"
daten["Deckung"] = 2e+6
daten["Währung"] = "EURO"
inhaber = dict()
inhaber["Name"] = "Mustermann"
inhaber["Name"] = "Max"
inhaber["männlich"] = True
hobbys = list()
hobbys.append("Reiten")
hobbys.append("Golfen")
hobbys.append("Lesen")
inhaber["Hobbys"] = hobbys
inhaber["Alter"] = 42
inhaber["Kinder"] = list()
inhaber["Partner"] = None
daten["Inhaber"] = inhaber

# Daten serialisieren
zeichenkette = json.dumps(daten, indent=4)
 
# ... irgendwann an anderer Stelle ... 

new_file = file('json.txt', 'a')
new_file.write(zeichenkette + "\n")
new_file.close()


print "hallo github"
# Daten deserialisieren
# erhalten = json.loads(zeichenkette)

# und ausgeben
# print erhalten