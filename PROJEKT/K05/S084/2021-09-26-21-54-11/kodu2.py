import string
from random import *
def suurväike(text):
    muudetud=""
    suvaline=string.punctuation[randint(0,len(string.punctuation)-1)]
    for char in text:
        if char.isupper():
            muudetud += char.lower()
        elif char.islower():
            muudetud += char.upper()
        elif string.punctuation.find(char) != -1:
            muudetud += suvaline
        else:
            muudetud += char
    return muudetud