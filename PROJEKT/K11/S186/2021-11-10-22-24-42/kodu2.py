def transponeeriK(maatriks):
    a=len(maatriks)
    b=len(maatriks[1])
    uusmaatriks=[]
    for m in range(0, b):
        temp=[]
        for n in range(0, a):
            temp.append('')
        uusmaatriks.append(temp)
    c=0
    for i in range(0, a):
        for j in range(0, b):
            uusmaatriks.insert([b-1-i+c][a-1-c], maatriks[i][j])
        c+=1
    return uusmaatriks
