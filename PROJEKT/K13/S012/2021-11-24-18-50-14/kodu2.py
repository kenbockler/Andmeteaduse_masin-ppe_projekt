from turtle import *
def fraktal(n, k�lg):
    if n == 1:
        for i in range(4):
            forward(k�lg)
            left(90)
            left(180)
    else:
        for i in range(4):
            forward(k�lg)
            left(90)
            if i < 3:
                fraktal(n-1, k�lg/2)
            left(180)
    