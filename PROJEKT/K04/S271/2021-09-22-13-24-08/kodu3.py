from turtle import *
from random import *
screen = Screen()
screen.screensize(500, 500)
screen.setup(500, 500)
def hulknurgad(külgede_arv, külje_pikkus):
    sisenurk = ((külgede_arv - 2) * 180) / külgede_arv
    for i in range(külgede_arv):
        color('navy')
        fd(külje_pikkus)
        lt(180 - sisenurk)
for i in range(30):
    penup()
    goto(randint(-400, 400), randint(-300, 300))
    pendown()
    hulknurgad(randint(3, 10), randint(10, 200))
turtle.exitonclick()
    