def transponeeriK(maatriks):
    uus1=[]
    uus2=[]
    uus3=[]
    for m in range(len(maatriks)):
        uus=[]
        sisu=maatriks[m]
        a=len(sisu)-1
        for n in range(len(sisu)):
            uus.append(sisu[a])
            a=a-1
        uus1.append(uus)
    for m in range(len(sisu)):
        uus_x=[]
        a=len(sisu)-1
        for n in range(len(uus1)):
            uus_x.append(uus1[n][m])
            a=a-1
        uus2.append(uus_x)
    for m in range(len(uus2)):
        uus_y=[]
        sisu=uus2[m]
        a=len(sisu)-1
        for n in range(len(sisu)):
            uus_y.append(sisu[a])
            a=a-1
        uus3.append(uus_y)
    print(uus3)
    return uus3
transponeeriK([[1, 2, 3],[4, 5, 6],[7, 8, 9]])