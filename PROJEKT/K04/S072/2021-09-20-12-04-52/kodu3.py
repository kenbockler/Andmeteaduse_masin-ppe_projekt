from turtle import *
from random import randint
speed()
def hulknurk(n, r):
    nurk = ((n - 2) * 180) / n
    while n > 0:
        forward(r * 50)
        right(180 - nurk)
        n -= 1
for _ in range(30):
    up()
    setpos(randint(-window_width() / 2 + 300, window_width() / 2 - 300), randint(-window_height() / 2 + 300, window_height() / 2 - 300))
    down()
    hulknurk(randint(3, 10), randint(1, 4))
exitonclick()