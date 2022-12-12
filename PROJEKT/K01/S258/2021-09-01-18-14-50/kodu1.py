from turtle import *
left(180)
forward(5)
left(180)
forward(5)
forward(100)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
left(90)
forward(50)
right(90)
forward(20)
x=0
while x!=90:
    right(1)
    forward(1)
    x+=1
forward(40)
x=0
while x!=72:
    right(1)
    forward(2)
    x+=1
right(18)
left(90)
up()
forward(500)
left(90)
forward(20)
left(90)
down()
n=0
while n!=5:
    x=0
    while x!=30:
        right(1)
        forward(2)
        x+=1
    x=0
    while x!=60:
        left(1)
        forward(2)
        x+=1
    x=0
    while x!=30:
        right(1)
        forward(2)
        x+=1
    n+=1
print("Valmis.")
exitonclick()