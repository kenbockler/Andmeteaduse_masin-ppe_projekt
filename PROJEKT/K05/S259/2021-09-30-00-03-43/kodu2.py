import string
from random import*
def suurväike(sõne):
    b = randint(0, len(string.punctuation)-1)
    asendus = string.punctuation[b]
    a = ""
    for i in sõne:
        if i in string.punctuation:
            a = a + asendus
        else:
            a = a + i
    return a.swapcase()