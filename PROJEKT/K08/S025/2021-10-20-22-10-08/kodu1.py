from random import sample
def bingo():
    while True:
        a = sample(range(1, 11), 3)
        b = sample(range(11, 21), 2)
        j�rjend = a + b
        if 1 in j�rjend and 2 in j�rjend and 3 in j�rjend:
            continue
        else:
            return j�rjend