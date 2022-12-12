from turtle import *
import random
def kujund(n, a):
    if n <= 2:
        raise Exception("Külegde arv hulknurga joonistamiseks on liiga väike")
    s=(n-2)*180
    üks = s/n
    pööre = 180-üks
    while n > 0:
        forward(a)
        left(pööre)
        n -= 1
x = 30
while x > 0:
    n=random.randint(3, 10)
    a=random.uniform(6, 20)
    kujund(n, a)
    up()
    pööre = random.randrange(1, 360, 15)
    left(pööre)
    edasi = random.randrange(int(a), int(a)+100)
    forward(edasi)
    down()
    x-=1
exitonclick()