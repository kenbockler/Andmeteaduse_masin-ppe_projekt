from random import randint
def minu_shuffle(a):
    indeksid = len(a)
    for i in range(indeksid):
        rand = randint(i, indeksid - 1)
        a[i], a[rand] = a[rand], a[i]
    return a
try :
    x = []
    while True:
        x.append(int(input()))
except :
    print(minu_shuffle(x))