






x =int(input("Zadejte číslo dne v týdnu:"))


if x == 1:
    print("pondělí")
elif x == 2:
    print("úterý")
elif x == 3:
    print("středa")
elif x == 4:
    print("čtvrtek")
elif x == 5:
    print("pátek")
elif x == 6:
    print("sobota")
elif x == 7:
    print("neděle")
else:
    print("Tolik dnů nemáme")


y =int(input("Zadejte číslo měsíce v kalendářním roce:"))

if  (3 <= y <= 5):
    print("Jaro")
elif  (6 <= y <= 8):
    print("Léto")
elif  (9 <= y <= 11):
    print("Podzim")
elif  (12 <= y <= 2):
    print("Zima")

if (1 <= y <= 6):
    print("1. pololetí")
elif (6 <= y <= 12):
    print("2. pololetí")
else:
    print("Tolik pololetí nemáme")





