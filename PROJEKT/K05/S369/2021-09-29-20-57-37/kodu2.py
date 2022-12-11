import string
import random
symbol = string.punctuation
m2rk = symbol[random.randint(0, len(symbol)-1)]
def suurväike(lause):
    for i in lause:
        if i in symbol:
            lause = lause.replace(i, m2rk)
    return lause.swapcase()
print(suurväike("Aias sadas saia, Leiba ja Peedi-Porgandi pehmikut."))
    