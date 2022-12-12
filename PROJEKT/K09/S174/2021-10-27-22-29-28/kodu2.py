from random import randint
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        suvaline_indeks = randint(0,len(järjend) - 1)
        järjend[i], järjend[suvaline_indeks] = järjend[suvaline_indeks], järjend[i]