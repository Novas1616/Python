

def vypis_soucet(x):
    for cislo in range(1, 6):
        soucet=cislo+x
        krat=cislo*x
        print(f"{cislo}+{x}={soucet}, {cislo}*{x}={krat}")

x=int(input("Zadej číslo kterým budeme násobit:"))
vypis_soucet(x)