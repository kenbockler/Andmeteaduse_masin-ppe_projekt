from turtle import*
def fraktal(sügavus):
    if sügavus == 0:
        return None
    elif sügavus > 1:
        forward(100)
        left(90)
        fraktal(sügavus-1)
        forward(50)
        if sügavus > 2:
            left(90)
            forward(25)
            if sügavus > 3:
                left(90)
                forward(12)
    elif sügavus == 1:
        for i in range(4):
            forward(100)
            left(90)
fraktal(4)