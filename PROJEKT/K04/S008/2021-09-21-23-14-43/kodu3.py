from turtle import *
from random import randint
i = 0
def hulknurk (x, y):
    joonistatud_k�ljed = 0
    while joonistatud_k�ljed < x:
        forward (y)
        right (360/x)
        joonistatud_k�ljed +=1
while i < 30:
    hulknurk (randint(3, 10), randint(10, 20))
    up ()
    randomNumber = randint (1,2)
    if randomNumber == 1:
        left(randint(0, 360))
    else:
        right(randint(0, 360))
    forward(randint(0, 100))
    down()
    i += 1