cena_za_ks = float(input("Zadej cenu:"))
pocet_ks = float(input("Zadej počet kusů:"))
dan = 21

celkova_cena = cena_za_ks * pocet_ks
dan = (celkova_cena/ 100) * dan
cena_po_zdaneni = celkova_cena + dan

print("cena před zdaněním:", celkova_cena, "Kč")
print("daň:", dan, "Kč")
print("Cena po zdanění:", cena_po_zdaneni, "Kč")


