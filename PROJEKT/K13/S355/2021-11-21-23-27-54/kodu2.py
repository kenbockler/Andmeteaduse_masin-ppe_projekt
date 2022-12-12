from turtle import Turtle, Screen
def fraktaal(level, t, pikkus, direction = 90):
    for elem in range(3):
        t.forward(pikkus)
        if level > 1:
            fraktaal(level-1, t, pikkus/2, -direction)
        t.right(direction)
    t.forward(pikkus)
    t.right(direction)
screen = Screen()
t = Turtle()
t.speed(10)
fraktaal(4,t, 100)
screen.exitonclick()