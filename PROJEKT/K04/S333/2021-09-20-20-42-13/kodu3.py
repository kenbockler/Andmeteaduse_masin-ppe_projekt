from turtle import *
import random
def hulknurk(külje_pikkus,külgede_arv):
    i=0
    speed(10)
    delay(0)
    penup()
    forward((külje_pikkus/2))
    pendown()
    while i< külgede_arv:
        right(360/külgede_arv)
        forward(külje_pikkus)
        i+= 1
i=0
while i<30:
    külje_pikkus= random.randint(1,200)
    külgede_arv= random.randint(3,20)
    hulknurk(külje_pikkus, külgede_arv)
    penup()
    n= (random.randint(1,2))
    if n==1:
        left(random.randint(0,360))
    else:
        right(random.randint(0,360))
    m= (random.randint(1,2))
    if m==1:
        forward(random.randint(1,200))
    else:
        backward(random.randint(1,200))
    i +=1
    pendown()
exitonclick()