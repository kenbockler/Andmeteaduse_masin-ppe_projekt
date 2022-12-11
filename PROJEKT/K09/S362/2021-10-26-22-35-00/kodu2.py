from random import *
def minu_shuffle(a1):
    for i in range(len(a1)):
        j=randint(0,len(a1)-1)
        kustutatav=a1.pop(j)
        a1+=[kustutatav]
a1 = [1, 3, 3, 4, 5, 5, 5, 6, 6]