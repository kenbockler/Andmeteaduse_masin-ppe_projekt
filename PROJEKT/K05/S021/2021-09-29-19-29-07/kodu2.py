import string
import random
def suurv�ike(a):
    t�hed = a.swapcase()
    asendus = random.choice(string.punctuation)
    l�plik = t�hed
    for x in t�hed:
        if x in string.punctuation:
            l�plik = l�plik.replace(x, asendus)
    return l�plik 
muudetud=suurv�ike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut.")
print(muudetud)
    