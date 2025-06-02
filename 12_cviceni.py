pocet_ks= float(input("Zadej počet kusů:"))
cena_za_ks= float(input("Zadej cenu jednoho kusu:"))
sleva= float(input("zadejte hodnotu slevy:"))

celkova_suma= (pocet_ks * cena_za_ks)
velikost_slevy= (celkova_suma/100 )* sleva
cena_po_sleve= celkova_suma - velikost_slevy

print("cena bez slevy je:", celkova_suma, "kč")
print("Sleva je:" ,velikost_slevy, "Kč")
print("cena po slevě je:" ,cena_po_sleve, "Kč")