from turtle import *
from random import randint
def hulknurk(arv, pikkus):
    joonistatud_külgi = 0
    penup()
    goto(randint(-300, 300), randint(-300, 300))
    pendown()
    while joonistatud_külgi < arv:
        forward(pikkus)
        left(360 / arv)
        joonistatud_külgi += 1
hulknurgad = 0
while hulknurgad < 30:
    random_arv = randint(3, 15)
    random_pikkus = randint(10, 100)
    hulknurk(random_arv, random_pikkus)
    hulknurgad += 1
exitonclick()