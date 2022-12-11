from turtle import*
from random import randrange
h = 1
while h <= 30:
    h += 1
    küljed = randrange(3,7)
    küljepikkus = randrange(50,100)
    def joonis(küljed, küljepikkus):
        i = 0
        penup()
        right(randrange(1,360))
        forward(randrange(50,100))
        pendown()
        while i < küljed:
            i += 1
            forward(küljepikkus)
            right(360/küljed)
    print(joonis(küljed, küljepikkus))
exitonclick()
