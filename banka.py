x = input("Zadej jméno: ")
y = int(input("Zadej zůstatek: "))

def vyber(castka):
    global y
    if castka > y:
        print("Nemáš dostatečný zůstatek")
    elif castka <= 0:
        print("Částka musí být větší než 0 Kč")
    else:
        y -= castka
        print(f"Výběr úspěšný! Nový zůstatek je: {y} Kč")

def vklad(castka):
    global y
    if castka <= 0:
        print("Částka musí být větší než 0 Kč")
    else:
        y += castka
        print(f"Vloženo {castka} Kč. Nový zůstatek je: {y} Kč")

def kontrola():
    print(f"Zůstatek je: {y} Kč")

while True:
    print("\n1 - Výběr")
    print("2 - Vklad")
    print("3 - Zůstatek")
    print("4 - Konec")

    volba = int(input("Zadej číslo pro provedení operace: "))

    if volba == 1:
        castka = float(input("Zadejte částku k výběru: "))
        vyber(castka)
    elif volba == 2:
        castka = float(input("Zadejte částku k vkladu: "))
        vklad(castka)
    elif volba == 3:
        kontrola()
    elif volba == 4:
        print("Děkujeme za použití našeho systému. Nashledanou!")
        break
    else:
        print("Neplatná volba, zkuste to znovu.")
