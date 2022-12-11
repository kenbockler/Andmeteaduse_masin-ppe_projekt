from turtle import *
def poore(s = "p", k = 100, kn = 90, un = 6):
    if not(s == "p" or s == "v"):
        return 1
    uk = k / (kn/un)
    hk = 0
    while (k > hk):
        fd(uk)
        if (((hk*kn/k)+un) > kn):
            un = kn-(hk*kn/k)
        hk += uk
        if (s == "p"):
            rt(un)
        if (s == "v"):
            lt(un)
forward(100)
poore(s = "v", k = 200, kn = 60)
lt(120)
forward(30)
lt(90)
forward(20)
rt(90)
forward(270.25)
rt(90)
forward(300)
rt(90)
poore(kn = 45, k = 100)
poore(kn = 45, k = 200)
rt(90)
forward(180.03)
lt(90)
forward(73.53)
rt(90)
forward(100)
rt(90)
forward(20)
lt(90)
forward(30)
lt(120)
poore(s = "v", k = 166, kn = 60)
forward(30)
