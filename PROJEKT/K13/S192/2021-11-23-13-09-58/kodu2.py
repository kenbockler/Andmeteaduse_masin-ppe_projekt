from turtle import *
def fraktal(sügavus, pikkus):
    s = sügavus
    p = pikkus
    if s == 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            left(180)
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(s - 1, pikkus * 0.5)
            left(180)
            