from turtle import *
from math import *
colormode(255)
Turtle()
pencolor(11,19,245)
pendown()
forward(250)
right(135)
forward(100)
right(45)
forward(250 - 2*100*cos(radians(45)))
right(45)
forward(100)
penup()
right(135)
forward(125)
left(90)
pencolor(0,0,0)
pendown()
forward(200)
right(150)
forward(150/cos(radians(30)))
right(120)
forward(150*tan(radians(30)))