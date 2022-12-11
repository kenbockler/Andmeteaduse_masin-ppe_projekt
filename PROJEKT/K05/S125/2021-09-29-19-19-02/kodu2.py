from random import *
import string
sõne = input("Sisesta lause/sõna: ")
märgid = string.punctuation
def suurväike(sõne):
    sõne = sõne.swapcase()
    number = randint(0, 31)
    märk = märgid[number]
    for i in sõne:
        if i in märgid and i != märk:
            sõne = sõne.replace(i, märk)
    return sõne
print(suurväike(sõne))