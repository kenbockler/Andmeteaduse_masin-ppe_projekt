from turtle import forward, right, left, back, up, down
import random
joonistatud_k�lgi == 0
k�lgede_arv == str(random())
k�lgede_pikkus == float(random())
def hulknurk(k�lgede_arv, k�lgede_pikkus):
    while joonistatud_k�lgi < k�ldege_arv:
        forward(k�lgede_pikkus)
        left((k�lgede_arv-2)*180/k�lgede_arv)
        joonistatud_k�lgi += 1
def edasi():
    up()
    forward(100)
    left(90)
    forward(100)
    down()
joonisatud_kujundid == 0
while joonistatud_kujundid < 30
    hulknurk(k�lgede_arv, k�lgede_pikkus)
    edasi()
    joonisatud_kujundid += 1
exitonclick()
