from random import sample
def bingo():
    bingo1 = []
    bingo2 = []
    bingo1.extend(sample(range(1, 11), 3))
    if sum(bingo1) == 6:
        bingo1.clear()
        bingo1.extend(sample(range(1, 11), 3))
    bingo2.extend(sample(range(11, 21), 2))
    bingo3 = bingo1 + bingo2
    return bingo3
print(bingo())
    