from random import randint
def minu_shuffle(j�rjend):
    for i in range(len(j�rjend)-1,0,-1):
        juhuslik = randint(0, i+1)
        j�rjend[i], j�rjend[juhuslik] = j�rjend[juhuslik], j�rjend[i]
    print(j�rjend)
minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6])