def transponeeriK(maatriks):
    maatriksT = []
    for i in range(len(maatriks[0])):
        rida = []
        for j in range(len(maatriks)):
            rida.append(maatriks[len(maatriks)-1-j][len(maatriks[0])-1-i])
        maatriksT.append(rida)        
    return maatriksT