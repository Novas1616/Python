import random

print("najdi tajné číslo")
pokusy=0
max_pokusy=3
x=random.randint(1,10)


while pokusy<max_pokusy:
    odpoved=int(input("váš tip:"))
    pokusy+=1
    if odpoved<x or odpoved>x:
        print("Tohle není správné číslo")
    else:
        print("Vyhral jsi")
        break
if pokusy == max_pokusy:
    print("vyčerpali jste všechny pokusy",max_pokusy," tajné ščíslo bylo", x)