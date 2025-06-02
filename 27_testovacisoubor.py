print("Jsem tvůj alkohol tester")
pohlavi=str(input("Zadej svoje pohlaví:"))
cas=int(input("zadej pred jakou dobou jsi mel pivo:"))

if pohlavi == "muž" and cas<180:
    print("Za volant můžeš za", 3*60-cas, "minut")
elif cas>180:
    print("už můžeš řídit")
elif pohlavi == "žena" and cas<240:
    print("Za volant můžeš za", 4*60-cas, "minut")
elif cas>240:
    print("už můžeš řídit")
else:
    print("pohlaví není definováno")