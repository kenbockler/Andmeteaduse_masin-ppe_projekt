def transponeeriK(maatriks):
    uus = []
    for rida in range(2,-1,-1):
        elemendid = []
        for j in range(1,-1,-1):
            elemendid.append(maatriks[j][rida])
        uus.append(elemendid)
    print(uus)
print(transponeeriK([[4, 31, 67, 99]]))
