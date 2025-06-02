import turtle


turtle.penup()
turtle.backward(200)
turtle.pendown()
turtle.speed(0)
turtle.pencolor("yellow")
turtle.bgcolor("black")
turtle.pensize(5)


for i in range(6):
    for j in range(6):
        turtle.forward(60)
        turtle.left(60)

    turtle.forward(60)
    turtle.right(60)

turtle.exitonclick()