from turtle import *

speed(0)
color("yellow")
pensize(5)
begin_fill()
bgcolor("blue")

home()
circle(50)
end_fill()


for i in range(10):
    setpos(0,50)
    forward(200)
    backward(400)
    left(18)

begin_fill()

for j in range(6):
    pensize(3)
    color("lightgray")
    circle(30)
    penup()
    forward(40)
    pendown()
    for k in range(4):
        circle(20)
        left(90)

end_fill()

exitonclick()