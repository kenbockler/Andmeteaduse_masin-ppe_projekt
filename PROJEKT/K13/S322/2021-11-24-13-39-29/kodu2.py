from turtle import *
def ruudud(suurus, hulk):
    if hulk > 0:
        for i in range(3):
            forward(suurus)
            right(90)
            ruudud(-suurus/2, hulk-1)
        forward(suurus)
        right(90)