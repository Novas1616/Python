# operátory se pomocí závorek samozřejmě dají kombinovat




cislo = int(input("Zadejte číslo v rozmezí 10-20 nebo 30-40: "))
if (cislo >= 10) and (cislo <= 20) or ((cislo >=30) and (cislo <= 40)):
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")