from random import sample
j�rjend = []
def bingo():
    x = sample(range(1,11),3)
    while sum(x) == 6:
        x = sample(range(1,11),3)
    y = sample(range(11,21),2)
    j�rjend = x + y 
    return j�rjend
    