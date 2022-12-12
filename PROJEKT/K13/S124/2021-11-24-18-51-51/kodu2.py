from turtle import *
def fraktal(sügavus, pikkus, suund=90):
    speed('fastest')
    for i in range(3):
        forward(pikkus)
        if sügavus > 1:
            fraktal(sügavus - 1, pikkus/2, -suund)
        right(suund)
    forward(pikkus)
    right(suund)
