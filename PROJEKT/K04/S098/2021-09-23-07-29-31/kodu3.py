from turtle import *
import random
def ruut(e,f):
    joonistatud_kylgi = f
    while joonistatud_kylgi >0:
        left(180-((((f-2)*180)/f)))
        forward(e)
        joonistatud_kylgi += -1
e=(random.randint(10,100))
f=(random.randint(3,6))
i=30
while i>0:
    ruut(e,f)
    up()
    right(random.randint(0,360))
    forward(random.randint(10,120))
    left(90)
    forward(100)
    down()
    i=i-1
exitonclick()
