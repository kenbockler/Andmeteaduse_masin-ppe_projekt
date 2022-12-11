from random import randint
def minu_shuffle(järjend):
    for el in range(len(järjend)-1, 0, -1):
        i = randint(0, el)
        järjend[el], järjend[i] = järjend[i], järjend[el]
        