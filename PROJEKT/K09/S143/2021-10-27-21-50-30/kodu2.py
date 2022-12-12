from random import randint
def minu_shuffle(l):
    for i in range(len(l)):
        a = l[i]
        c = randint(0,len(l)-1)
        b = l[c]
        l[i] = b
        l[c] = a
