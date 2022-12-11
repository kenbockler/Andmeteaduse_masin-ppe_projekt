import random
import string
def suurväike (a):
    b = random.choice(string.punctuation)
    vastus = ""
    for taht in a:
        if taht.isupper() is True:
            taht = taht.lower()
            vastus = vastus + taht
        elif taht.islower() is True:
            taht = taht.upper()
            vastus = vastus + taht
        elif taht == " ":
            vastus = vastus + taht
        elif taht != b:
            taht = b
            vastus = vastus + taht
        elif taht == b:
            vastus = vastus + taht
    return vastus