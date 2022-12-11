def transponeeriK(maatriks):
    transpmaatriks = []
    for veerg in range(len(maatriks[0])-1, -1, -1):
        uus_rida = []
        for rida in range(len(maatriks)-1, -1, -1):
            uus_rida.append(maatriks[rida][veerg])
        transpmaatriks.append(uus_rida)
    return transpmaatriks
