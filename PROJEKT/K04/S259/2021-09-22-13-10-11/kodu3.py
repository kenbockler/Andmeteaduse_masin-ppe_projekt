from turtle import*
from random import randint
hulknurk = 0
def hulknurk(nurgad, külg):
    i = 0
    while i < nurgad:
        i += 1
        fd(külg)
        right(360/nurgad)
hulk = 0
while hulk < 30:
    hulk += 1
    penup()
    goto(randint(-300, 250), randint(-300, 250))
    pendown()
    hulknurg(randint(3, 20), randint(10,60))
