import string
import random
def suurv�ike(s�ne):
    vahetus = s�ne.swapcase()
    s�mbol = random.choice(string.punctuation)
    uus = ""
    for t�ht in vahetus:
        if t�ht in string.punctuation:
            t�ht = s�mbol
            uus += t�ht
        else:
            t�ht = t�ht
            uus += t�ht
    return uus
    