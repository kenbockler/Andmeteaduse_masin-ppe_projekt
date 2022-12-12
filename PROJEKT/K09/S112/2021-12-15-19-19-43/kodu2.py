from random import randint
a = [1,2,3,4,5,6]
def minu_shuffle(a):
    for arv in range(len(a) - 1, 0, -1):
        uus = randint(0,arv)
        if uus == arv:
            continue
        a[arv],a[uus] = a[uus],a[arv]
minu_shuffle(a)
print(a)
