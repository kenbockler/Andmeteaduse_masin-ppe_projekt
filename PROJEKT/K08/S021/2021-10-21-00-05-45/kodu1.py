from random import sample
def bingo():
    j�rjend1 = sample(range(1, 11), 3)
    if 1 in j�rjend1 and 2 in j�rjend1 and 3 in j�rjend1:
        return bingo()
    else:
        pass
    j�rjend2 = sample(range(11, 21), 2)
    j�rjend = j�rjend1 + j�rjend2
    return j�rjend
bingo()
    