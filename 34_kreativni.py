from turtle import *
from random import *

colormode(255)


speed(0)


pensize(5)
for i in range(18):
    for j in range(6):
        for i in range(10):
            bgcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
            pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
            forward(10)
        left(60)
        forward(10)
    left(20)



exitonclick()