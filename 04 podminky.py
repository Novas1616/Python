



cislo = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (cislo > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit! ")
    odmocnina = cislo ** (1/2)
    print("Odmocnina z čísla", cislo, "je", odmocnina)
if (cislo <= 0):
    print("Odmocnina ze záporného čísla a nuly neexistuje!")
print("Děkuji za zadání")