# napište program, který vypíše hlášku:
# Zadej číslo a pokud je pravda, že číslo je větší než pět
# vypiš - správně, zadal jsi číslo větší než 5!

cislo = int(input("Zadej nějaké číslo: "))
if (cislo > 5):
    print("správně, zadal jsi číslo větší než 5!")
if (cislo < 5):
    print("špatně, zadal jsi číslo menší než 5")
print("Děkuji za zadání")