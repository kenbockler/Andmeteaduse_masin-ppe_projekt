import string
import random
def suurv�ike(s�ne):
    uus = ""
    m�rk = random.choice(string.punctuation)
    for t�ht in s�ne:
        if t�ht in string.punctuation:
            t�ht = m�rk
            uus += t�ht
        elif t�ht == t�ht.upper():
            t�ht = t�ht.lower()
            uus += t�ht
        elif t�ht == t�ht.lower():
            t�ht = t�ht.upper()
            uus += t�ht
    return uus
            