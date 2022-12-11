from random import randint
def minu_shuffle(a):
    ring = 0
    while ring is not (len(a)+1):
        ring += 1
        if a == []:
            a = []
        else:
            juhuslik_indeks1 = randint(0, (len(a)-1))
            juhuslik_indeks2 = randint(0, (len(a)-1))
            a[juhuslik_indeks1], a[juhuslik_indeks2] = a[juhuslik_indeks2], a[juhuslik_indeks1]