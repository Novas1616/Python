import turtle

turtle.speed(0)
turtle.pencolor("red")
turtle.bgcolor("black")
turtle.pensize(5)
for i in range(18):
    for j in range(6):
        turtle.left(60)
        turtle.forward(100)
    turtle.left(20)


turtle.color("yellow")
turtle.pensize(5)
turtle.begin_fill()
for u in range(18):
    for h in range(6):
        turtle.left(60)
        turtle.forward(20)
    turtle.left(20)
turtle.end_fill()
turtle.exitonclick()