from turtle import *
from random import *

colormode(255)
pensize(5)
speed(0)



for i in range(995):
     for j in range(5):
         bgcolor("black")
         pencolor((randint(0,255), randint(0,255), randint(0,255)))
         forward(80)
         left(30)
     forward(10)
     left(39)
     forward(100)
     right(100)
     left(130)


exitonclick()