'''-- Kodutöö nr. 13 - 2. Sarnaste ruutude fraktal --'''
import turtle
def ruutude_fraktal(pikkus, sügavus):
    if sügavus <= 0:
        return
    for i in range(3):
        turtle.forward(pikkus)
        turtle.left(90)
        ruutude_fraktal(pikkus//2, sügavus - 1)
        turtle.left(180)
    turtle.forward(pikkus)
    turtle.left(90)
    turtle.left(180)
turtle.speed('fast')
turtle.pensize(2)
ruutude_fraktal(200, 3)
turtle.exitonclick()
turtle.done()