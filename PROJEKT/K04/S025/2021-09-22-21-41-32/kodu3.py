from turtle import *
import random
def hulknurk(k�lgede_arv, k�ljepikkus):
    p��rde_kraad = 360 // k�lgede_arv
    while k�lgede_arv > 0:
        forward(k�ljepikkus)
        left(p��rde_kraad)
        k�lgede_arv -= 1
i = 30
while i > 0:
    i -= 1
    hulknurk(random.randint(3,10), random.randint(20,100))
    a = random.randint(20,100)
    b = random.randint(1,360)
    c = random.randint(20,100)
    up()
    forward(a)
    left(b)
    forward(c)
    down()
exitonclick()