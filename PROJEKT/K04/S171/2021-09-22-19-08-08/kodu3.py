from turtle import*
from random import*
n = int(input())
a = int(input())
def hulknurk(x, y):
    for i in range(0,x):
        forward(y)
        right(180-(x-2)*(180/x))
hulknurk(n, a)
