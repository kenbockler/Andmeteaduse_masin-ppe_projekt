from turtle import *
def joonista_ruut(s�gavus):
    global nurk, pikkus
    if s�gavus >= 1:
        for _ in range(3):
            forward(pikkus)
            pikkus = pikkus/2
            nurk = - nurk
            joonista_ruut(s�gavus - 1)
            pikkus = pikkus * 2
            nurk = - nurk
            right(nurk)
        forward(pikkus)
        right(nurk)
pikkus = 200
nurk = 90
joonista_ruut(10)