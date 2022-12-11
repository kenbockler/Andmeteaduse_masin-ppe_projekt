def transponeeriK(maatriks):
    uusmaatriks=[]
    veerge=len(maatriks)
    ridu=len(maatriks[0])
    for i in range(ridu-1,-1,-1):
        lisa=[]
        for j in range(veerge-1,-1,-1):
            lisa.append(maatriks[j][i])
        uusmaatriks.append(lisa)
    return uusmaatriks
print(transponeeriK([[4, 31, 67, 99]]))