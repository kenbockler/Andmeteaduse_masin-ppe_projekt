from random import randint
def minu_shuffle(j�r):
    i = 0
    for i in range(len(j�r)):
        juhuslik1 = randint(0, (len(j�r)-1))
        juhuslik2 = randint(0, (len(j�r)-1))
        j�r[juhuslik1], j�r[juhuslik2] = j�r[juhuslik2], j�r[juhuslik1]
        i += 1