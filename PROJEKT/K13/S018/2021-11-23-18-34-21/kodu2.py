from turtle import *
def knruut(serv,s�g):
    speed(10)
    if s�g >= 1:
        forward(serv)
        left(90)
        knruut(serv*0.5,s�g-1)
        right(180)
        forward(serv)
        left(90)
        knruut(serv*0.5,s�g-1)
        right(180)
        forward(serv)
        left(90)
        knruut(serv*0.5,s�g-1)
        right(180)
        forward(serv)
        right(90)
knruut(100,3)
