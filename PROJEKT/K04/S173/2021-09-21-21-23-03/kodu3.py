from turtle import*
from random import*
def f(a, b):
    x=a
    while x>0:
        forward(b)
        right(360/a)
        x-=1
speed(0)
z=30
while z>0:
    a = randint(3, 20)
    b = randint(5, 100)
    f(a, b)
    penup()
    home()
    right(randint(0, 360))
    forward(randint(1, 300))
    pendown()
    z-=1
exitonclick()