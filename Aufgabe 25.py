#Aus Platzgründen werde ich die einzelnen Teilaufgaben hier nicht aufzählen. Stattdessen habe ich versucht es mit Kommentaren auszugleichen, danke

class Guest:#Erstellen der Klasse "Guest"
    def __init__(self, tischnummer):#Definieren der Attribute
        self.tischnummer = tischnummer
        self.bestellungen = []#Noch keine Bestellungen
        self.betrag = 0.0#noch kein Betrag da noch keine Bestellungen

    def bestellen(self, gericht):
        if gericht in menue:#Falls das Bestellte Gericht im Menü vorhanden ist
            preis = menue[gericht]#Beziehe den Preis
            self.bestellungen.append(gericht)#Packe ihn in die Bestellung
            self.betrag += preis#Erhöhe den Betrag um die das bestellte
            print(f"{gericht} bestellt.")#sage welches Gericht bestellt wurde
        else:
            print(f"{gericht} existert nicht auf der Speisekarte!")#Wenn das Gericht nicht im Menü vorhanden ist

    def ausgabe_daten(self):#Ausgabe der Daten des Gasts
        print(f"Tischnummer: {self.tischnummer}")#Tischnummer
        print("Bestellte Speisen und Getränke:")#Die bestellten Getränke und Speisen
        for bestellung in self.bestellungen:
            print(f"- {bestellung}")
        print(f"Das macht dann bitte: {self.betrag} Euro. Danke und guten Appetit!")#Der Insgesamte zu zahlende Preis

#Speisekarte
menue = {'Pasta': 5.00, 'Lasagne': 7.50, 'Coca Cola': 1.50, 'Pepsi': 1.80,
'Schnitzel mit Pommes': 8.00, 'Salat Ceasar Style': 3.70}

#Gast erstellen und Bestellungen aufgeben
guest1 = Guest(1)
guest1.bestellen('Salat Ceasar Style')
guest1.bestellen('Lasagne')
guest1.bestellen('Coca Cola')
guest1.bestellen('Nudelauflauf')


#Daten des Gastes ausgeben
guest1.ausgabe_daten()
