import turtle

turtle.penup()
turtle.backward(200)
turtle.pendown()
turtle.speed(0)
turtle.pencolor("yellow")
turtle.bgcolor("black")
turtle.pensize(5)

for j in range(4):
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)




turtle.exitonclick()