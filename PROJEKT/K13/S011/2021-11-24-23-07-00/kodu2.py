from turtle import *
def ruut(k�lg,s�gavus):
    if s�gavus == 1 :
        forward(k�lg)
        right(90)
        forward(k�lg)
        right(90)
        forward(k�lg)
        right(90)
        forward(k�lg)
        right(90)
    else:
        forward(k�lg)
        ruut(k�lg*0.5,s�gavus-1)
        left(90)
        forward(k�lg)
        ruut(k�lg*0.5,s�gavus-1)
        left(90)
        forward(k�lg)
        ruut(k�lg*0.5,s�gavus-1)
        left(90)
        forward(k�lg)
        left(90)
    