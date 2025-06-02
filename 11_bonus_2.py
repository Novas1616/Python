cena_za_ks = float(input("Zadej cenu za 1 ks:"))
pocet_ks = float(input("Zadej počet ks:"))
sleva_procenta=float(input("Zadej slevu:"))

celkova_cena = cena_za_ks * pocet_ks
sleva_v_penezich = (sleva_procenta/ 100) * celkova_cena
cena_po_sleve = celkova_cena - sleva_v_penezich

print("cena před slevou:", celkova_cena, "Kč")
print("sleva:", sleva_v_penezich, "Kč")
print("cena po slevě:", cena_po_sleve, "Kč")


