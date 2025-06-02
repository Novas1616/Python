#kdyz vypisujeme pomoci print() vice hodnot, dela se mezi nimi automatickypauza.
print("AAAA",5,"AAA")
print()

#pokud tuto mezeru nechceme, da se udelat napr. pomoci metody str().
#ktera konvertuje jakoukoliv predanou hodnotu na string.
#stringy se daji pote spojovat pomoci operatoru +.
#timto zpusobem vlastne funkci print predavame
#jedinou hodnotu, a proto se tam neobjevuji mezery.

s="aaaaa"+str(5)+"bbbbb"
print(s)

#nebo také takto
print("AAAA"+str(5)+"BBBB")
print()


#druha oznost je upravit parametr sep (separator). Ten je defalutne nastaven na " " (mezeru)
#což je důvod, proč se mezi více hodnotami vypisuje automaticka mezera.
#z toho duvodu nam staci upravit jaho hodnotu na prazdny sting ("")
#toho se da vyuzit v situlaci, kdy chceme mezi hodnotami vypisovat i jine veci napr zalamovat radek

print("AAAA", 5,1, "bbbb",sep="")

#zalamovani radku
print("(#####\|/####)", 3546, "fsafs", 45, sep="\n")