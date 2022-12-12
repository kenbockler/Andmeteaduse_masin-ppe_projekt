import random
import string
sõne = input("Sisesta midagi: ")
def suurväike(sõne):
    märk = string.punctuation
    vahetus = random.choice(märk)
    for i in range (len(sõne)):
        if sõne[i] in märk:
            sõne = sõne.replace(sõne[i], vahetus)
    return(sõne.swapcase())
print(suurväike(sõne))
    