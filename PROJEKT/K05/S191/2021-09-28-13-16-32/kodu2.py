import random
import string
def suurväike(fraas):
    invert=""
    märk=random.choice(string.punctuation)
    for i in fraas:
        if i.islower()==True:
            invert+=i.upper()
        elif i.isupper()==True:
            invert+=i.lower()
        elif i==" ":
            invert+=i
        else:
            i=märk
            invert+=i
    return invert