import string
märgid = string.punctuation
from random import randint
def suurväike(sõne):
    sõne = sõne.swapcase()
    suvanr = märgid[randint(0,31)]
    while True:
        for i in sõne:
            if i in märgid and i != suvanr:
                sõne = sõne.replace(i, suvanr)
        return sõne
print(suurväike(str(input("Sisesta midagi: "))))
