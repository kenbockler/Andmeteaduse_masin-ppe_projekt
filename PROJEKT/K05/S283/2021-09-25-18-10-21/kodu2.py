import random
import string
def suurväike(sõne):
    uus_sõne = ""
    märgid = string.punctuation
    suvaline_märk = random.choice(string.punctuation)
    for i in sõne:
        if i.isupper():
            uus_sõne += i.lower()
        elif i.islower():
            uus_sõne += i.upper()
        elif i == " ":
            uus_sõne += " "
        elif i in märgid:
            uus_sõne += suvaline_märk
    return uus_sõne
sõne_sisend = input("Palun sisestage sõne: ")
print(suurväike(sõne_sisend))