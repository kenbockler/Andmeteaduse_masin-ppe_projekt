from turtle import *
def hulk_nurk(arv, pikkus):
    for i in range(arv):
        forward(pikkus)
        right(360 / arv)
arv = int(input('Sisestage küldege arv: '))
pikkus = int(input('Sisestage külje pikkus: '))
hulk_nurk(arv, pikkus)
exitonclick()