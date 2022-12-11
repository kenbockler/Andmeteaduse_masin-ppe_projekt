import random
import string
random = random.choice(string.punctuation)
tekst=input("Sisesta mingi lause: ")
def suurväike(tekst):
    suursõna=''
    for suur in tekst:
        if suur.isupper():
            suursõna+=suur.lower()
        if suur.islower():
            suursõna+=suur.upper()
        if suur.isspace():
            suursõna+=' '
        if suur in string.punctuation:
            suursõna+=random
    print(suursõna)
suurväike(tekst)
