import random
def minu_shuffle(j�rjend):
    for i in range(len(j�rjend)):
        vahetatav = random.choice(range(len(j�rjend)))
        j�rjend[i], j�rjend[vahetatav] = j�rjend[vahetatav], j�rjend[i]
    print(j�rjend)
minu_shuffle([1, 2, 3, 4])
