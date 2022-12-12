def transponeeriK(maatriks):
    transponeeritud = []
    i = len(maatriks[0]) - 1
    j = len(maatriks) - 1
    for rida in range(i,-1,-1):
        rida_uus = []
        for veerg in range(j,-1,-1):
            rida_uus += [maatriks[veerg][rida]]
        transponeeritud += [rida_uus]
    return transponeeritud