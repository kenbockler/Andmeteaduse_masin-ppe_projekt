def transponeeriK(maatriks):
    uus_maatriks = []
    veergude_arv = len(maatriks[0])
    ridade_arv = len(maatriks)
    for i in range(veergude_arv - 1, -1, -1):
        veerg = []
        for j in range(ridade_arv - 1, -1, -1):
            veerg.append(maatriks[j][i])
        uus_maatriks.append(veerg)
    return uus_maatriks      