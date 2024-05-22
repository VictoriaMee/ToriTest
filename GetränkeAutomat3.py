#Für den Kauf mehrerer Flaschen EINER Sorte MIT Wechselgeld
#Behobene Probleme: Absturz beim direkten Zahlen der vollen Summe.
#Neues Problem: Gibt Wechselgeld mit "-" Vorzeichen an...


#definition der Funktion zur Bestellung
def multiOrder():
    print ("Bitte wähle ein Getränk:")
    #Usereingabe des Getränkes
    getraenk = int(input("1. Wasser (0.50€)\n2. Limonade (1.00€)\n3. Bier (2.00€)\n"))
    getraenkMenge = int(input("Bitte wählen Sie, wie viele Flaschen Sie möchten!\n"))
    
    #bestimmt nicht die eleganteste Lösung..System prüft die User-Eingabe und gleicht ab
    #Im Prinzip der Ersatz für einen Switch-Case
    
    if getraenk == 1:#änderung 0 auf 5 zum testen
        betrag = 0.50 * getraenkMenge #Kosten pro Flasche * gewählte Menge
        print (betrag,"€")
        zahlung = float(input("Gewähltes Getränk: Wasser.\nBitte werfen Sie den oben stehenden Betrag in Euro oder Cent Münzen ein.\n"))
        rest = betrag - zahlung#Zur Berechnung vom Rest, wird der Betrag

        while rest > 0.00:
            print(f"\nEs fehlen noch {rest} Euro")
            rest -= float(input(f"Brauche mehr Geld: \n"))
        while rest == 0.00:
            print(f"\nVielen Dank, bitte entnehmen Sie Ihr Getränk.")
            return
        while rest < 0.00:
            print(f"\nVielen Dank, bitte entnehmen Sie Ihr Getränk. Ihr Wechselgeld beläuft sich auf {rest} Euro.")
            return
            
 
    elif getraenk == 2:
        betrag = 1.00 * getraenkMenge #Kosten pro Flasche * gewählte Menge
        print (betrag,"€")
        zahlung = float(input("Gewähltes Getränk: Limonade.\nBitte werfen Sie den oben stehenden Betrag in Euro oder Cent Münzen ein.\n"))
        rest = betrag - zahlung#Zur Berechnung vom Rest, wird der Betrag - dem schon gezahlten gerechnet

        while rest > 0.00:
            print(f"\nEs fehlen noch {rest} Euro")
            rest -= float(input(f"Brauche mehr Geld: \n"))
        while rest == 0.00:
            print(f"\nVielen Dank, bitte entnehmen Sie Ihr Getränk.")
            return
        while rest < 0.00:
            print(f"\nVielen Dank, bitte entnehmen Sie Ihr Getränk. Ihr Wechselgeld beläuft sich auf {rest} Euro.")
            return
            
        
        
    elif getraenk == 3:
        betrag = 2.00 * getraenkMenge #Kosten pro Flasche * gewählte Menge
        print (betrag,"€")
        zahlung = float(input("Gewähltes Getränk: Bier.\nBitte werfen Sie den oben stehenden Betrag in Euro oder Cent Münzen ein.\n"))
        rest = betrag - zahlung#Zur Berechnung vom Rest, wird der Betrag

        while rest > 0.00:
            print(f"\nEs fehlen noch {rest} Euro")
            rest -= float(input(f"Brauche mehr Geld: \n"))
        while rest == 0.00:
            print(f"\nVielen Dank, bitte entnehmen Sie Ihr Getränk.")
            return
        while rest < 0.00:
            print(f"\nVielen Dank, bitte entnehmen Sie Ihr Getränk. Ihr Wechselgeld beläuft sich auf {rest} Euro.")
            return
  
    else:
        print("Getränk nicht vorhanden. Bitte wählen Sie eines der vorhandenen Getränke aus!\n")
        multiOrder()
        

multiOrder()
