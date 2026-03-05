# Start

R = 0   # Variable zum Hochzählen der Räume
gesamtflaeche = 0.0   # float, weil Fläche Kommazahlen haben kann

weiter = "j"   # Variable für die while Schleife

while weiter == "j":
    print("\nNeuer Raum wird erfasst.")
    R = R + 1  # Raumzahl erhöhen
    print("Raumnummer:", R)
    raumflaeche = 0.0  # Variable zum Berechnen und Ausgeben der Raumfläche
    teilflaechen = input("Besteht der Raum aus mehreren Teilflächen? (j/n): ")
    if teilflaechen == "j":
        anzahl_teilflaechen = int(input("Wie viele rechteckige "
                                        "Teilflächen hat der Raum? "))
    else:
        anzahl_teilflaechen = 1
    for i in range(anzahl_teilflaechen):
        if teilflaechen == "j":
            print("\nTeilfläche", i + 1)
        laenge = float(input("Länge in Metern eingeben: ").replace(",", "."))
        breite = float(input("Breite in Metern eingeben: ").replace(",", "."))
        teilflaeche = laenge * breite
        if anzahl_teilflaechen >= 2:
            print("Teilfläche:", teilflaeche, "m²")
            raumflaeche = raumflaeche + teilflaeche
    print("\nRaumfläche:", raumflaeche, "m²")
    gesamtflaeche = gesamtflaeche + raumflaeche
    weiter = input("\nGibt es einen weiteren Raum? (j/n): ")

# Durchschnitt berechnen
if R > 0:
    durchschnitt = gesamtflaeche / R
    print("\nGesamtfläche:", gesamtflaeche, "m²")
    print("Anzahl Räume:", R)
    print("Durchschnittliche Raumgröße:", durchschnitt, "m²")
else:
    print("Es wurden keine Räume erfasst.")

# Ende
