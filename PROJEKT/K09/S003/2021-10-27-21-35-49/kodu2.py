from random import randint
def minu_shuffle(j�rjend):
    for i in range(len(j�rjend)):
        element = j�rjend.pop(randint(0,len(j�rjend)-1))
        j�rjend.append(element)
