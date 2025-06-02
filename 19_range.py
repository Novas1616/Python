#Generování posloupnosti čísel

#Využijeme další standartní funkci range(),
#pomocí které budeme zejména ve for-cyklech generovat,
#různé posloupnosti hodnot:
#Tato funkce může mít různý počet parametrů
#a podle toho se bude generována i výsledná posloupnost:
#Všechny parametry musí být celočíselné.

#funkce range()

#range(stop)
#range(start,stop)
#range(start,stop,krok)

#parametry:
#start()- první prvek vygenerované posloupnosti (pokud chybí, předpokládá se 0)
#stop - hodnota na ní se již generované další hodnoty posloupnosti zastavé- tato hodnota již v posloupnosti nebude
#krok- hodnota, o kterou se zvýší (resp. sníží pro záporný krok) každý následující prvek posloupnosti,
#pokud tento parametr chybí, předpokládá se 1

#Většinou platí, že do parametru stop nastavíme o 1 větší hodnotu než tu,
#co chceme jako poslední hodnotu generované posloupnosti

#Nejlépe si to ukážeme na příkladech různých vygenerovaných posloupnostích celých čísel. V tabulce vidíme výsledky pro
#různé parametry:

#range(10)               0,1,2,3,4,5,6,7,8,9
#range(0,10)             0,1,2,3,4,5,6,7,8,9
#range(0,10,1)           0,1,2,3,4,5,6,7,8,9
#range(3,10)             3,,4,5,6,7,8,9
#range(3,10,2)           3,5,7,9
#range(10,100,10)        10,20,30,40,50,60,70,80,90
#range(10,1,-1)          10,9,8,7,6,5,4,3,2
#range(10,1)             prázdná posloupnost
#range(1,1)              prázdná posloupnost
