import turtle 
def ruudud(n, k�lg):
    if n == 0:
        return n
    elif n == 1:
        for i in range(4):
            turtle.forward(k�lg)
            turtle.left(90)
            turtle.left(180)
    else:
        ruudud(n-1,k�lg)
        m = k�lg
        for i in range(4):
            turtle.forward(k�lg)
            turtle.left(90)
            if i < 3:
                m = m/2
                for i in range(4):
                    turtle.forward(m)
                    turtle.left(90)
                    turtle.left(180)
            turtle.left(180)
         