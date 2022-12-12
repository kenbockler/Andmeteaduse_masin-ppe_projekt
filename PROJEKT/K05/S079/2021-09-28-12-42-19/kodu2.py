import random
import string
def suurväike(sõne):
    rndm = random.choice(string.punctuation)
    uus_sõne = ""
    for s in sõne:
        if s.isupper():
            s = s.lower()
            uus_sõne += s
        elif s.islower():
            s = s.upper()
            uus_sõne += s
        elif s.isnumeric():
            uus_sõne += s
        elif s == " ":
            uus_sõne += s
        else:
            s = rndm
            uus_sõne += s
    return uus_sõne