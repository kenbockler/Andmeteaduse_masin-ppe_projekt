from turtle import*
from random import randint
speed(0)
k�lgede_arv=randint(3, 40)
k�ljepikkus=randint(10, 150)
j=0
suvaline_nurk=randint(0, 360)
suvaline_distants=randint(0, 500)
kordaja=randint(0, 1)
def hulknurk(k�lgede_arv, k�ljepikkus):
    i=0
    while i < k�lgede_arv:
        fd(k�ljepikkus)
        right(180+(k�lgede_arv - 2) * 180 / k�lgede_arv)
        i+=1
while j < 30:
    k�lgede_arv=randint(3, 40)
    k�ljepikkus=randint(10, 150)
    hulknurk(k�lgede_arv, k�ljepikkus)
    up()
    if kordaja == 1:
        left(suvaline_nurk +180)
    else:
        right(suvaline_nurk + 180)
    fd(suvaline_distants)
    down()
    j+=1