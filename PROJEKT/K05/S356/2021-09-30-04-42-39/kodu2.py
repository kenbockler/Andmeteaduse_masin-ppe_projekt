import random
import string
def suurväike (a):
    vahetus = []
    b = random.choice(string.punctuation)
    vastus = ''
    symbol = set(string.punctuation)
    for i in a:
        if i == ' ':
            vahetus.append(' ')
        elif i.isupper():
            vahetus.append(i.lower())
        elif i.islower():
            vahetus.append(i.upper())
        elif any(s in symbol for s in i):
            vahetus.append(b)
    return vastus.join(vahetus) 