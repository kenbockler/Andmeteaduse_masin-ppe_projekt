import string
import random
import re
def suurväike(sõne):
    l = ""
    i = 0
    uus_sümbol = random.choice('!"
    while i < len(sõne):
        sümbol = sõne[i]
        if sümbol.isalpha():
            if sümbol.isupper():
                sümbol = sümbol.lower()
            else:
                sümbol = sümbol.upper()
        elif sümbol in string.punctuation:
            sümbol = sümbol.replace(sümbol, uus_sümbol)
        i += 1
        l += sümbol
    return l
    