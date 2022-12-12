from turtle import *
import random
def koht():
    up()
    x = random.randint(-450,450)
    setx(x)
    y = random.randint(-450,450)
    sety(y)
    down()
def joonistus(arv, pikkus):
    koht()
    f = 0
    nurk = ((arv-2) * 180)/arv
    float(nurk)
    nurk = 180-nurk
    while f!=arv:
        forward(pikkus)
        left(nurk)
        f =f+ 1
    return
a = 0
while a < 30:
    hideturtle()
    hulk = random.randint(3,10)
    mõõt = random.randint(15,30)
    joonistus(hulk,mõõt)
    a = a + 1
exitonclick()
