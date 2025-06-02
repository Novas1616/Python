from turtle import *
from random import *

colormode(255)

pensize(5)



for i in range(6):
    for j in range(6):
        for j in range(10):
            pencolor((randint(0,255), randint(0,255), randint(0,255)))
            forward(10)
        left(60)
    penup()
    forward(100)
    right(60)
    pendown()
exitonclick()