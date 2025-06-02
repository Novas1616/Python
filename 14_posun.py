text=input("Zadej svůj řetězec:")

y= int(input("Zadej posun:"))

def dalsi_pismeno():
    zprava=""

    for znak in text.lower():
        kod=ord(znak)
        kod+=y
        if (kod>ord("z")):
            kod=kod-26
        zprava+=chr(kod)

    print("původní zpráva:", text)
    return zprava

print("Nová zpráva:", dalsi_pismeno())