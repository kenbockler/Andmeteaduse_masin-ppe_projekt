from random import sample
def bingo():
    tulemus = []
    c = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    a = []
    while True:
        a = sample(range(1, 11), 3)
        if a not in c:
            tulemus = tulemus + a
            break
    b = sample(range(11, 21), 2)
    tulemus = tulemus + b
    return tulemus