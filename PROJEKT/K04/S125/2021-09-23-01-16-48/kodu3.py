from random import *
from turtle import *
def hulknurk(külgede_arv, küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        left(360 / külgede_arv)
        joonistatud_külgi += 1
hulknurki = 0
while hulknurki < 30:
    juhuslik_x = randint(-400, 400)
    juhuslik_y = randint(-400, 400)
    külgede_arv = randint(3, 10)
    küljepikkus = randint(20, 45)
    up()
    goto(juhuslik_x, juhuslik_y)
    down()
    hulknurk(külgede_arv, küljepikkus)
    hulknurki += 1
speed("fastest")
exitonclick()