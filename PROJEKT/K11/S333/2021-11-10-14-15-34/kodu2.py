def transponeeriK(maatriks):
    uus=[]
    rida=[]
    for i in range(-1,-(len(maatriks[0])+1),-1):
        for j in range(-1,-(len(maatriks)+1),-1):
            rida.append(maatriks[j][i])
        uus.insert(-i,rida[:])
        rida.clear()
    return uus
