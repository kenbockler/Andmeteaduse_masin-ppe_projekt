from random import sample
def bingo():
    j�rj1 = sample(range(1, 11), 3)
    while (1 in j�rj1) and (2 in j�rj1) and (3 in j�rj1):
        j�rj1 = sample(range(1, 11), 3)
    j�rj2 = sample(range(11, 21), 2)
    j�rjend = j�rj1 + j�rj2
    return j�rjend
                   