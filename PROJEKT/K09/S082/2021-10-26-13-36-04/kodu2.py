from random import randint
def minu_shuffle(nimekiri):
    vahepealne = []
    for a in nimekiri:
        n = randint(0,1)
        if n == 0:
            True
        elif n==1:
            vahepealne = nimekiri
            x = randint(0, len(nimekiri)-1)
            vahetatav = nimekiri[x]
            nimekiri[nimekiri.index(a)] = vahetatav
            nimekiri[x] = a
nimekiri = [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(nimekiri)