def transponeeriK (maatriks):
    maatriks_tulemus = []
    a = len(maatriks[0])
    for el in maatriks:
        if a!= len(el):
            print("Error.")
            return
    for i in range(len(maatriks[0])):
        rida =[]
        for j in range(len(maatriks)):
            rida.append(maatriks[j][i])
        rida2 = rida[::-1]
        maatriks_tulemus.append(rida2)
    return maatriks_tulemus[::-1]
    