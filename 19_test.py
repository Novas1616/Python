#Napiš program, který:
#Načte od uživatele vstupní řetězec.
#Zjistí, jak je řetězec dlouhý.
#Převede všechny znaky na velká písmena.
#Spočítá, kolikrát se v řetězci vyskytuje určitý znak (uživatel si ho zadá).
#Obrátí celý řetězec naopak.
#Vybere první tři znaky a připojí k nim text "Python je super!".

def analyzuj_retezec():
    retezec = input("Zadejte řetězec: ")

    print("Délka řetězce:", len(retezec))
    print("Řetězec velkými písmeny:", {retezec.upper()})

    znak = input("Zadejte znak, který chcete spočítat: ")
    print(f"Znak '{znak}' se v řetězci vyskytuje {retezec.count(znak)}×")

    print("Obrácený řetězec:", {retezec[::-1]})
    print("Výsledek:", retezec[:3], "Python je super!")

analyzuj_retezec()