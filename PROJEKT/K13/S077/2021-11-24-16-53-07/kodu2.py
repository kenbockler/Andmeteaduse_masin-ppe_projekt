from turtle import *
speed(0)
def fraktal(sügavus,pikkus):
    if sügavus>=1:
        for i in range(4):
            forward(pikkus)
            left(90)
            if sügavus>1:
                if i<3:
                    left(180)
                    fraktal(sügavus-1,pikkus/2)
                    right(180)
left(90)
up()
forward(150)
right(180)
down()
fraktal(4,300)
exitonclick()