import string
from random import randint
def suurv�ike(s�ne):
    i=0
    suvaline_indeks=randint(0, 31)
    tulemus=string.punctuation
    tulemus2=tulemus[suvaline_indeks]
    muudetud_s�ne=s�ne.swapcase()
    while i<32:
        muudetud_s�ne=muudetud_s�ne.replace(tulemus[i], tulemus2)
        i+=1
    return muudetud_s�ne