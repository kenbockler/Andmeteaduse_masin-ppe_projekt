import random
def minu_shuffle(a):
    n=len(a)
    for i in range(n):
        j=random.randint(0, n-1)
        kustuta=a.pop(j)
        a.append(kustuta)