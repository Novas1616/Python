#Uživatel zadá libovolný text.
#program převede všechna písmena na malá písmena.
#Spočítá, kolikrát se v řetězci vyskytuje písmeno "a".
#Obrátí pořadí znaků v řetězci.
#Nahrazení mezer znakem -

x=input("Zadej řetězec:")

def text():
    print(x.lower())
    print(x.count("a"))
    print(x[::-1])
    print(x.replace(" ", "-"))

text()