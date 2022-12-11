import turtle
import random
turtle.speed(10)
turtle.delay(0)
def hulknurk(sidecount, sidelength):
    nurgakraad = 360 / sidecount
    for i in range(sidecount):
        turtle.forward(sidelength)
        turtle.right(nurgakraad)
for n in range(0, 31):
    hulknurk(random.randrange(3, 12), random.randrange(10, 50))
    turtle.up()
    turtle.right(random.randrange(1, 360))
    turtle.forward(random.randint(75, 100))
    turtle.down()
turtle.exitonclick()