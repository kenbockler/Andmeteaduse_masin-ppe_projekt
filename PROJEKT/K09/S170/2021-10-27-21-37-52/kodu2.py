from random import randint
def minu_shuffle(a):
    pikkus = len(a)
    a[0], a[1] = a[randint(0, pikkus)], a[randint(0, pikkus)]
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(minu_shuffle(a))