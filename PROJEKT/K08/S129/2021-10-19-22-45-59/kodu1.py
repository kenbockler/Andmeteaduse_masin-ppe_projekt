from random import sample
def bingo():
    x = sample(range(1,11), 3)
    y = sample(range(11, 21), 2)
    numbrid = x + y
    if len(set(numbrid) & {1, 2, 3}) < 3:
        return numbrid
    else:
        return bingo()
print(bingo())
