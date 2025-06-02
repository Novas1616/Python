print("jsem tvuj alkoholtester")
pohlavi = str(input("Zadej jestli jsi muž nebo žena:"))
cas=int(input("Před jakou dobou jsi měl pivo:"))

if pohlavi=="muž" and cas<180:
    print("za volant muzes za", 3*60-cas, "minut")
elif cas>180:
    print("můžeš řídit")
if pohlavi=="žena" and cas<240:
    print("za volant muzes za", 4*60-cas, "minut")
elif cas>240:
    print("můžeš řídit")
else:
    print("pohlaví nedefinováno")