def transponeeriK(maatriks):
    uus = []
    for i in range(len(maatriks[0])-1, -1, -1):
        t�hi = []
        for j in range(len(maatriks)-1, -1, -1):
            t�hi += [maatriks[j][i]]
        uus.append(t�hi)
    return uus