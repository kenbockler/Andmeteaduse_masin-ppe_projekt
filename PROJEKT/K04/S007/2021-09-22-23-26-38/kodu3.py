from turtle import *
from random import randint
speed(1000000)
def f(k�lgede_arv, k�ljepikkus):
    nurk = 360/k�lgede_arv
    while k�lgede_arv > 0:
        forward(k�ljepikkus)
        left(nurk)
        k�lgede_arv -=1
i=0      
while i <30:
    f(randint(3,15), randint(1,100))
    up()
    setpos(randint(-100,200),randint(-100,200))
    down()
    i+=1
exitonclick()
