from random import randint
from random import shuffle
def minu_shuffle(a):
    for i in range(0, len(a)):
        arv = randint(0, len(a)-1)
        a[i], a[arv] = a[arv], a[i]