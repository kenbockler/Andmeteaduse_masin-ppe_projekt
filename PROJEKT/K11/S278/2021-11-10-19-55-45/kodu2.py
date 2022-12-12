def transponeeriK(x):
    uusmatriks = []
    for i in range(len(x[0])):
        row = []
        for j in range(len(x)):
            row.append(x[j][i])
        uusrow = row[::-1]
        uusmatriks.append(uusrow)
    return uusmatriks[::-1]
