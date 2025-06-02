#převádění typů
#co ale kdyz nechcemepracovat s řetězcem
#ale třeba s číslem? tady nám pomůže skupina
#funkci, ktera umi prevadet cisla na retezce
#a zpatky. kazdy ze tri typu
#(anglicky types) promnenych, ktere zatim zname
#ma funkci. ktera vezme nejakou hodnotu
#a vrati podobnout hodnotu "sveho" typu
#Na cela cisla je funkce int
#na realna cisla je float a pro retezce je str
#int(x)     #prevod na cele cislo
#float(x)   #prevod na realne cislo
#str(x)     #prevod na retezec



#priklady:



3==int("3")==int(3.0)==int(3.141)==int(3)
8.12==float("8.12")==float(8.12)
8.0==float(8)==float("8")==float(8.0)
"3"==str(3)==str("3")
"3,41"==str(3.141)==str("3,141")

# ne všechny převody jsou možné :
int("blablablabla")#chyba
float("blablablabla")# chyba
int("8,9")         #chyba