from turtle import *
from random import randint
def kujund(k�lgede_arv, k�ljepikkus):
    joonistatud_k�lgi = 0
    while joonistatud_k�lgi < k�lgede_arv:
        forward(k�ljepikkus)
        left(360/k�lgede_arv)
        joonistatud_k�lgi +=1
i=0
while i<=30:
    i += 1
    kujund(randint(3,10), randint(20,100))
    up()
    goto(randint(-100, 100),randint(-100, 100))
    down()
exitonclick()
