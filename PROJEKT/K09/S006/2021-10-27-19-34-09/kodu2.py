from random import randint 
def minu_shuffle(j�rjend):
    for element in j�rjend:
        juhuslik_indeks1 = randint(0, len(j�rjend)-1)
        juhuslik_indeks2 = randint(0, len(j�rjend)-1)
        j�rjend[juhuslik_indeks1], j�rjend[juhuslik_indeks2] = \
        j�rjend[juhuslik_indeks2], j�rjend[juhuslik_indeks1]
        