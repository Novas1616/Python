text=input("Zadej svůj řetězec:")

def dalsi_pismeno():
    zprava=""

    for znak in text.lower():
        kod=ord(znak)
        kod+=1
        if (kod>ord("z")):
            kod=kod-26
        zprava+=chr(kod)

    return zprava

print(dalsi_pismeno())