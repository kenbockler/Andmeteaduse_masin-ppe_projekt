import string
from random import choice
def suurv�ike(s�na):
    vahem�rk = choice(string.punctuation)
    for i in s�na:
        if i in string.punctuation:
            s�na = s�na.replace(i, vahem�rk)
    s�na = s�na.swapcase()
    return s�na
