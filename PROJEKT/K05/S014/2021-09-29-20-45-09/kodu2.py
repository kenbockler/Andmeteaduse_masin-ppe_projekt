import string
import random
lause=input("Sisesta lause: ")
m�rk=string.punctuation
uus_m�rk=random.choice(m�rk)
def suurv�ike(lause):
    lause=lause.swapcase()
    for i in lause:
        if i in string.punctuation:
            lause=lause.replace(i, uus_m�rk)
    return lause
print(suurv�ike(lause))
