def transponeeriK(maatriks):
    uus_maatriks = []
    for i in range(len(maatriks[0]) - 1, -1, -1):
        järjend = []
        for j in range(len(maatriks) - 1, -1, -1):
            järjend.append(maatriks[j][i])
        uus_maatriks.append(järjend)
    return uus_maatriks