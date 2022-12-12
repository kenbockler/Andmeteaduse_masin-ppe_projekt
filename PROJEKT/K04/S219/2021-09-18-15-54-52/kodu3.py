from turtle import *
from random import *
def hulknurk(n, pikkus):
    for x in range(n):
        forward(pikkus)
        left(360/n)
i = 0
while i < 30:
    hulknurk(randint(1, 50), randrange(1, 100))
    penup()
    right(randrange(1, 100))
    forward(randrange(1, 100))
    pendown()
    