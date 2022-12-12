def transponeeriK(maatriks):
    ridu = len(maatriks)
    tulpasid = len(maatriks[0])
    ajutine_rida = []
    transponeeritud = []
    for i in range(1, 1 + tulpasid):
        for j in range(1, 1 + ridu):
            ajutine_rida.append(maatriks[-j][-i])
        transponeeritud.append(ajutine_rida)
        ajutine_rida = []
    return transponeeritud