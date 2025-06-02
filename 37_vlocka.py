from turtle import *

bgcolor("blue")
pencolor("white")

speed(0)
pensize(5)
for i in range(8):
    setpos(0,0)
    forward(200)
    right(45)
    forward(50)
    backward(50)
exitonclick()