from turtle import*
speed(200)
def sügavus(külg, arv, nurk):
    color("red")
    begin_fill()
    for i in range(3):
        forward(külg)
        if arv > 1:
            külg = külg / 2
            nurk = -nurk
            sügavus(külg, arv - 1,  nurk)
            nurk = -nurk
            külg = külg * 2
        right(nurk)
    forward(külg)
    end_fill()
    right(nurk)
    color("green")
    begin_fill()
    end_fill()
sügavus(100, 4, 90)