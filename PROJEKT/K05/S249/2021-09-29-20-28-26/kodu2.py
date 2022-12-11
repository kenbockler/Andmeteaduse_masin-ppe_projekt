import string
import random
def suurväike(sõne):
    uus = ""
    uus_märk = str(random.choice(string.punctuation))
    for täht in sõne:
        if täht.isupper() == True:
            uus += täht.lower()
        elif täht in string.punctuation:
            uus += uus_märk
        else:
            uus += täht.upper()       
    return uus