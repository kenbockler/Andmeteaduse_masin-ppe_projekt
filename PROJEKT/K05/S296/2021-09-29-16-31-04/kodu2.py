import random
import string
kirjavahemärgid = '''!"
def suurväike(sõne):
    muutus= random.choice(kirjavahemärgid)
    for i in sõne:
        if i in string.punctuation:
            sõne = sõne.replace(i, muutus)
    sõne = sõne.swapcase()
    return sõne