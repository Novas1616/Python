from turtle import *
from random import *

colormode(255)
pensize(5)

speed(0)
pencolor("red")
bgcolor("black")
pensize(5)
for i in range(18):
    for j in range(6):
        pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        left(60)
        forward(100)
    left(20)



exitonclick()