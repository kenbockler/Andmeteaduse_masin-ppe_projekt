import string
import random
def suurväike(sõne):
    a = random.choice(string.punctuation)
    for el in sõne:
        if el in string.punctuation:
            sõne = sõne.replace(el, a)
    return sõne.swapcase()
print(suurväike("MuL?LE Me%ElDib pUL2GakOmm