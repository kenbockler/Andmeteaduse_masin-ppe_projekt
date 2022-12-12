from random import *
minu_jarjend = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(minu_jarjend):
    for el in range(len(minu_jarjend)):
        shuffle = randint(0, len(minu_jarjend)-1)
        uus = minu_jarjend[shuffle]
        minu_jarjend[shuffle] = minu_jarjend[el]
        minu_jarjend[el] = uus
