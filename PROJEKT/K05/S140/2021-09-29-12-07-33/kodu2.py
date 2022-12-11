import string
import random
def suurväike(word):
    sõna = ""
    märk = random.choice(string.punctuation)
    for i in word:
        if i == " ":
            sõna += " "
        elif i.isupper():
            sõna += i.lower()
        elif i.islower():
            sõna += i.upper()
        elif i in string.punctuation:
            i = märk
            sõna += i
    return sõna
