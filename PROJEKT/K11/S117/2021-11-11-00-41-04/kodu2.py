def transponeeriK(maatriks):
    t_maatriks = []
    for i in range(len(maatriks[0])):
        jarjend = []
        for j in range(len(maatriks)): 
            jarjend.append(maatriks[j][i])
        t_maatriks.append(jarjend[::-1])
    return t_maatriks[::-1]