from random import randint
def minu_shuffle(a):
    indeksid = []
    for i in range(len(a)):
        indeksid.append(i)
    uus_indeks = []
    while len(uus_indeks) < len(indeksid):
        idx = randint(0, len(a)-1)
        if idx not in uus_indeks:
            uus_indeks.append(idx)
            continue
        else:
            continue
    a[:] = [a[i] for i in uus_indeks]
    print(a)