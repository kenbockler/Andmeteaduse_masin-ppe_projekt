from string import punctuation
from random import choice 
def suurväike(sõne):
    a=sõne.swapcase()
    for i in a:
        if i in punctuation:
            a=a.replace(i,".") 
    a=a.replace(".",choice(punctuation))
    return a
