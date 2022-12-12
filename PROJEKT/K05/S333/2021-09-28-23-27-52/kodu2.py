import string
import random
def suurväike(sõne) :
    sõne= sõne.swapcase()
    sümbolid= (string.punctuation)
    lõpp= len(string.punctuation)-1
    juhus= random.randint(0,lõpp)
    for märk in sõne:
        if märk in sümbolid:
            sõne= sõne.replace(märk,sümbolid[juhus])
    return sõne
