from turtle import *
from random import randint
k = 1
while k < 31:
    k += 1
    k�lgede_arv = randint(3, 20)
    k�ljepikkus = randint(15, 50)
    def hulknurk(k�lgede_arv, k�ljepikkus):
        i = 0
        nurk = 360 / k�lgede_arv
        while (i < k�lgede_arv):
            forward(k�ljepikkus)
            left(nurk)
            i = i + 1
    hulknurk(k�lgede_arv, k�ljepikkus)
    up()
    left(randint(0, 360))
    forward(randint(0, 150))
    down()
exitonclick()
