from turtle import *
def fun(n, p):
    if n >= 1:
        for i in range(4):
            forward(p)
            left(90)
            if i< 3:
                fun(n-1, p/2)
            left(180)
speed(0)
fun(2, 100)