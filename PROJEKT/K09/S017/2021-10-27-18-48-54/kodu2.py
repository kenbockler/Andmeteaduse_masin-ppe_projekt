from random import randint
def minu_shuffle(j�rjend):
    el_arv = len(j�rjend)
    indeks = 0
    for el in j�rjend:
        juhuslik_arv = randint(0, el_arv - 1)
        j�rjend[indeks], j�rjend[juhuslik_arv] = j�rjend[juhuslik_arv], j�rjend[indeks]
        indeks += 1
