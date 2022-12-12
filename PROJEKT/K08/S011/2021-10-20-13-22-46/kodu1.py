from random import sample
def bingo():
    numbrid = []
    num_10 = sample(range(1,11), 3)
    numbrid = numbrid + num_10
    while numbrid == [1, 2, 3] :
        numbrid = []
        num_10 = sample(range(1,11), 3)
        numbrid = numbrid + num_10
    num_20 = sample(range(10,21),2)
    numbrid = numbrid + num_20
    return numbrid
