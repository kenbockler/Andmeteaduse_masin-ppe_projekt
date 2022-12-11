def transponeeriK(maatriks):
    t = []
    a = []
    for el in maatriks:
        l = len(maatriks) - 1
        p = len(el) - 1
    for i in range(p, -1, -1):
       a = []
       for j in range(l, -1, -1):
           a += [maatriks[j][i]]
       t += [a]
    return t
