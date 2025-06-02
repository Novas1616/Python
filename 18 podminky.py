



a =int(input("Zadejte prvni cislo:"))
b =int(input("Zadejte druhe cislo:"))
c =int(input("Zadejte treti cislo:"))

if (a == b == c):
    print("Cisla jsou si rovna")
else:
    if a >= b and a>= c:
        print("Nejvetsi cislo je:", a)
    elif b >= a and b >= c:
        print("Nejvetsi cislo je:", b)
    else:
        print("Nejvetsi cislo je", c)



