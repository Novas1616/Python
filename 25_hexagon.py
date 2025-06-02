import turtle


turtle.color("red")
turtle.pensize(5)
turtle.begin_fill()


for j in range(6):
    turtle.left(60)
    turtle.forward(100)

turtle.end_fill()


turtle.exitonclick()