def transponeeriK(maatriks):
    n = len(maatriks)
    m = len(maatriks[0])
    uus_maatriks = []
    for i in range(m):
        tühi_rida = [0] * n
        uus_maatriks.append(tühi_rida)
    for i in range(n):
        for j in range(m):
            element = maatriks[i][j]
            uus_maatriks[m-j-1][n-i-1] = element
    return uus_maatriks
transponeeriK([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [1, 2, 0]])
