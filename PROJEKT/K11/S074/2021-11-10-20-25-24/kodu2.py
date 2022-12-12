def transponeeriK(maatriks):
    transponeeritud = []
    for rida in range(len(maatriks[0]) -1, -1, -1):
        transponeeritav = []
        for veerg in range(len(maatriks) -1, -1, -1):
            transponeeritav.append(maatriks[veerg][rida])
        transponeeritud.append(transponeeritav)
    return transponeeritud