from random import randint
x=0


while True:
    odpoved = input("\nchceš otočit kartu:")
    if odpoved == "ne":
        print("game over")
        break #ukončí program
              #a vyskočí z cyklu o úroveň výš

    else:
        karta=randint(1,10)
        x+=karta
        print("otočil jsi", karta, "tvůj počet bodů je",x)
        if x>21:
            print("prohra")
            break