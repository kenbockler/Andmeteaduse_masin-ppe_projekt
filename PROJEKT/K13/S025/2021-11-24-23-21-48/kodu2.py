from turtle import *
def t(s�gavus, k�lg):
    if s�gavus >= 1:
        for i in range(4):
            forward(k�lg)
            left(90)
            if i < 3:
                t(s�gavus - 1, k�lg / 2)
            left(180)