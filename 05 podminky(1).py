


print("Ta samá podmínka pomocí konstrukce if-else:")
cislo = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (cislo > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit! ")
    odmocnina = cislo ** (1/2)
    print("Odmocnina z čísla", cislo, "je", odmocnina)
else:
    print("Odmocnina ze záporného čísla a nuly neexistuje!")
print("Děkuji za zadání")

# rozdíl mezi dvěmi if-y a if + else:
#2 if-y za sebou: Postupně od prvního if-u provede test podmínek
#vždy se podívá u if-u na podmínku a bud ji splní nebo ne
#(bud je True nebo False)