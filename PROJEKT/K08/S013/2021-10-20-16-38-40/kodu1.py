from random import sample
def bingo():
    x = sample(range(1,11),3)
    y = sample(range(11,21),2)
    while sum(x) == 6:
        x = sample(range(1,11),3)
        if sum(x) > 6:
            break
        return x
    return (x + y)
print(bingo())