from turtle import *
def fraktal(arv,pikkus):
    forward(pikkus)
    if arv == 1:
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
    if arv > 1:
        fraktal(arv-1,pikkus*0.5)
        forward(pikkus)
        fraktal(arv-1,pikkus*0.5)
        forward(pikkus)
        fraktal(arv-1,pikkus*0.5)
        forward(pikkus)