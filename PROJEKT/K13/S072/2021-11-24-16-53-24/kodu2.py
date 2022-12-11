from turtle import *
speed(0)
def joonista_ruut(pikkus):
    for _ in range(4):
        forward(pikkus)
        left(90)
    left(180)
def fraktal(stoppsügavus, sügavus=1, pikkus=200):
    if sügavus == stoppsügavus:
        joonista_ruut(pikkus)
    else:
        if sügavus == 1 and stoppsügavus % 2 == 1:
            right(90)
        forward(pikkus)
        fraktal(stoppsügavus, sügavus=sügavus + 1, pikkus=pikkus * 0.5)
        left(90)
        forward(pikkus)
        fraktal(stoppsügavus, sügavus=sügavus + 1, pikkus=pikkus * 0.5)
        left(90)
        forward(pikkus)
        fraktal(stoppsügavus, sügavus=sügavus + 1, pikkus=pikkus * 0.5)
        left(90)
        forward(pikkus)
        right(90)
exitonclick()