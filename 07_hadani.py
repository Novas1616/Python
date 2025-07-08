import random

print("najdi tajné číslo")
pokusy=0
max_pokusy=10
x=random.randint(1,100)


while pokusy<max_pokusy:
    odpoved=int(input("váš tip:"))
    pokusy+=1
    if odpoved<x:
        print("Tvoje číslo je menší")
    elif odpoved>x:
        print("Tvoje číslo je větší")
    else:
        print("Vyhral jsi")
        break
if pokusy == max_pokusy:
    print("vyčerpali jste všechny pokusy",max_pokusy," tajné ščíslo bylo", x)