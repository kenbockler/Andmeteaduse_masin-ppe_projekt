def transponeeriK(maatriks):
    uus = []
    for i in range(len(maatriks[0])-1,-1,-1):
        tühi = []
        for j in range(len(maatriks)-1,-1,-1):
            tühi.append(maatriks[j][i])
        uus.append(tühi)
    return uus
maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transponeeriK(maatriks))