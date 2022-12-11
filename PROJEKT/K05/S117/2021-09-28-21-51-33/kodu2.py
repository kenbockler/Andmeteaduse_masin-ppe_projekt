import string
import random
def suurväike(sone):
    random1 = random.choice(list(string.punctuation))
    a = []
    for i in sone:
        if i in list(string.ascii_lowercase):
            i = i.upper()
            a.append(i)
        elif i in list(string.ascii_uppercase):
            i = i.lower()
            a.append(i)
        elif i in list(string.punctuation):
            a.append(random1)
        else:
            a.append(i)
    return(''.join(a))