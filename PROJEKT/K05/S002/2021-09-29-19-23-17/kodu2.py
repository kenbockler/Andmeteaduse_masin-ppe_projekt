from random import randint
from string import punctuation
def suurv�ike(a):
    b = ""
    koma = punctuation[randint(0, len(punctuation))]
    for i in a:
        if i.isupper():
            b += i.lower()
        elif i.islower():
            b += i.upper()
        elif i == " ":
            b += " "
        else:
            b += koma
    return b
print(suurv�ike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))