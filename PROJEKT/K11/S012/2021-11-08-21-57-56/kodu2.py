def transponeeriK(maatriks):
    read = len(maatriks)
    kolonnid = len(maatriks[0])
    uus_maatriks=[]
    for i in range(kolonnid):
        j‰rj = []
        for j in range(read):
            rida = read - j
            kolonn = kolonnid - i
            v‰‰rtus = maatriks[rida-1][kolonn-1]
            j‰rj.append(v‰‰rtus)
        uus_maatriks.append(j‰rj)
    return uus_maatriks
