b = input("xxxx")
pun = '!"
from random import*
f = choice(pun)
def suurv�ike(b):
    b = b.swapcase()
    for i in b:
        if i in pun:
            b = b.replace(i, f)
    return b
print(suurv�ike(b))