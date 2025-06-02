#ukazeme si dve funkce z modulu random
#ktere jsou velice uzitecne pro hry

#from random import randrange, uniform

#randrange(a,b)  #náhodné celé číslo od a do b-1
#uniform(a,b)    #náhodné reálné číslo od a do b
#randit(a,b)     #generuje náhodná čísla od a do b   (včetně a,b)

#protože jednotlivé složky barvy jsou čísla
#v rozmezi 0 az 255, pouzivame random.randit(0,255)

#pozor na to ze randage(a,b) nikdy nevrátí samotné b, pokud potrebujee nahodne vybrat ze tří možností

import random
cislo=random.randrange(0,3)
if cislo==0:
    print("kolečko")
elif cislo==1:
    print("Čtvereček")
else:
    print("trojůhelník")

#pamatuj, pokud importuješ z modulu
#random, nesmí se tvůj soubor jmenovat random.py
