from turtle import *
speed(0)
def fraktal(s�gavus, k�ljepikkus):
    if s�gavus == 1:
        for i in range(4):
            forward(k�ljepikkus)
            right(90)
        left(180)
    else:
        forward(k�ljepikkus)
        left(90)
        fraktal(s�gavus-1, k�ljepikkus/2)
        forward(k�ljepikkus)
        left(90)
        fraktal(s�gavus-1, k�ljepikkus/2)
        forward(k�ljepikkus)
        left(90)
        fraktal(s�gavus-1, k�ljepikkus/2)
        forward(k�ljepikkus)
        left(90)
fraktal(4, 100)
exitonclick()
        