from turtle import*
def fraktal(tase, pikkus):
    if tase == 0:
        return
    else :
        for i in range(1):
            forward(pikkus)
            left(90)
            fraktal(tase -1, pikkus *0.4)
            right(180)
            forward(pikkus)
            left(90)
            fraktal(tase -1, pikkus *0.4)
            right(180)
            forward(pikkus)
            left(90)
            fraktal(tase -1, pikkus *0.4)
            right(180)
            forward(pikkus)
            right(90)
            speed(100)
fraktal(4, 100)
