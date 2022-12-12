from turtle import *
def ruut_fraktal(ruut, pikkus, nurk):
    for i in range(3):
        fd(pikkus)
        if ruut > 1:
            pikkus = pikkus/2
            nurk = -nurk
            ruut_fraktal(ruut - 1,pikkus,nurk)
            nurk = -nurk
            pikkus *= 2
        right(nurk)
    forward(pikkus)
    right(nurk)
speed(300)
ruut_fraktal(5,100,90)
