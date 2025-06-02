from turtle import*
x=int(input("Zadej počet stran:"))

def mnohouhelnik():
    if x >=2:
        for i in range(x):
            left(360/x)
            forward(100)
        return

    else:
        print("zadej číslo větší než 2")
mnohouhelnik()
exitonclick()