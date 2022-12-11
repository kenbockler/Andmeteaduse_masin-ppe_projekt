import string
import random
def suurväike(sõna):
    sümbol = string.punctuation[random.randint(1, 32)]
    lõplik = ""
    for k in sõna:
        if k.islower():
            lõplik += k.upper()
        if k.isupper():
            lõplik += k.lower()
        if k in string.punctuation:
            lõplik += sümbol
        elif not k.islower() and not k.isupper() and k not in string.punctuation:
            lõplik += k
    return lõplik
