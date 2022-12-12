from random import sample
def bingo():
    checksum = 6
    first = sample(range(1, 11), 3)
    while True:
        summa = 0
        for el in first:
            summa += el
        if summa != checksum:
            break
        first = sample(range(1, 11), 3)
    return first + sample(range(11, 21), 2)
print(bingo())