import string
import random
def listmaker(makee):
    list1 = []
    list1[:0] = makee
    return list1
muut = listmaker(string.punctuation)
def suurväike(alg):
    suurused = alg.swapcase()
    juh = random.choice(string.punctuation)
    sv = suurused
    for i in muut:
            sv = sv.replace(i, juh)
    return sv
