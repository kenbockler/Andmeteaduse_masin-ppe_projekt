from turtle import*
speed(0)
def ruutfraktal(s�gavus, m��t):
    if s�gavus>1:
        for i in range(4):
            fd(m��t)
            left(90)
            if i <3:
                ruutfraktal(s�gavus-1, m��t/2)
                left(180)
        left(180)
    else:
        for i in range(4):
            fd(m��t/2)
            left(90)
            left(180)
ruutfraktal(4, 100)