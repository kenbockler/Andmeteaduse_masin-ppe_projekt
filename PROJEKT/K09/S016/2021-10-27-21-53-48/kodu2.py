from random import randint
def minu_shuffle(j�rjend):
    for el in j�rjend:
        suvaline_arv = randint(0, len(j�rjend)-1)
        suvaline_arv2 = randint(0, len(j�rjend)-1)
        j�rjend[suvaline_arv], j�rjend[suvaline_arv2] = j�rjend[suvaline_arv2], j�rjend[suvaline_arv]
    print(j�rjend)
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(minu_shuffle(a))