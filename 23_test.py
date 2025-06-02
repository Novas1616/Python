a=int(input("Zadejte první číslo:"))
b=int(input("Zadejte druhé číslo:"))
c=int(input("Zadejte třetí číslo:"))

if (a==b==c):
    print("Všechna čísla jsou shodná")
elif a>=b>=c:
    print("Největší je",a)
elif a<=b>=c:
    print("Největší je:", b)
else:
    print("Největší je:",c)