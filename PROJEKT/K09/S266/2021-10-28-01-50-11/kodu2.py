from random import randint
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        indeks2 = randint(0, len(järjend)-1)
        järjend[i], järjend[indeks2] =  järjend[indeks2], järjend[i]
        