while True:
    odpoved=input("\nZadejte odpověď ano nebo ne:")
    if odpoved == "ano" or odpoved == "ne":
        break #ukončí program
              #a vyskočí z cyklu o úroveň výš
    else:
        print("Špatně")
print("Díky")