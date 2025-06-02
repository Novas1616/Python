from turtle import *
delka=100
for s in range(5,9):
    for i in range(s):
        forward(delka/s)
        left(360 / s)
    penup()
    forward(delka)
    pendown()

exitonclick()