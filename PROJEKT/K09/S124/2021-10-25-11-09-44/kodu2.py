from random import sample, randint
import copy
def minu_shuffle(j):
    i = 0
    koopia = copy.deepcopy(j)
    indeksid = sample(range(0, len(j)), len(j))
    for indeks, element in zip(indeksid, j):
        j[i], koopia[indeks] = koopia[indeks], koopia[i]
        i += 1
