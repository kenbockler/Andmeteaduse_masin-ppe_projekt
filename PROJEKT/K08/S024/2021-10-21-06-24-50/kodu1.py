from random import sample
j�rjend = []
def bingo():
    arvud_1 = sample(range(1,11),3)
    if sum(arvud_1) == 6:
        arvud_1 = sample(range(1,11),3)
    arvud_2 = sample(range(11,21),2)
    j�rjend = arvud_1 + arvud_2
    return j�rjend