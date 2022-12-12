from random import randint
def minu_shuffle(a):
    n = 100
    for o in range(n):
        for i in range(len(a)):
            backup = a[i]
            asendatav = randint(0, len(a)-1)
            a[i] = a[asendatav]
            a[asendatav] = backup
