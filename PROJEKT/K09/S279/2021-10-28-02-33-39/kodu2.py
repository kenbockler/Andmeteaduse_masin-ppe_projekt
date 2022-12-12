from random import randint
def minu_shuffle(järjend):
    for indeks in range(len(järjend)):
        juhuslik_indeks = randint(0, indeks)
        if indeks == juhuslik_indeks:
            continue
        järjend[indeks], järjend[juhuslik_indeks] = järjend[juhuslik_indeks], järjend[indeks]