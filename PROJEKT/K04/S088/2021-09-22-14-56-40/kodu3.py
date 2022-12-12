from turtle import *
from random import randint
def hulknurk(u,v):
    pd()
    for i in range(u):
        forward(v)
        right(360 / u)
    up()
i = 0
speed(10)
while i < 30:
    up()
    x = randint(-360, 180)
    y = randint(-180, 360)
    a = randint(3, 10)
    b = randint(50, 200)
    setpos(x, y)
    hulknurk(a, b)
    i += 1
exitonclick()
    