def transponeeriK(maatriks):
    uus = []
    for i in reversed(range(len(maatriks[0]))):
        rida = []
        for j in reversed(range(len(maatriks))):
            rida.append(maatriks[j][i])
        uus.append(rida)
    return uus
print(transponeeriK([[4, 31, 67, 99]]))