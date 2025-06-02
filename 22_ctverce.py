import turtle

turtle.speed(0)
turtle.pencolor("yellow")
turtle.bgcolor("black")
turtle.pensize(5)
for i in range(18):
    for j in range(3):
        turtle.left(120)
        turtle.forward(200)
    turtle.left(20)

turtle.exitonclick()