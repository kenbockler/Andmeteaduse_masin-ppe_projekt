import string
import random
def suurv�ike(s�ne):
    uuss�ne = ""
    kirjavahem�rk = random.choice(string.punctuation)
    for i in s�ne:
        if i in string.punctuation:
            uuss�ne += kirjavahem�rk
        else:
            uuss�ne += i.swapcase()
    return uuss�ne
            