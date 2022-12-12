def transponeeriK(maatriks):
    Tmaatriks = []
    veerge = len(maatriks[0])
    ridu = len(maatriks)
    for i in range(ridu-1, -1, -1):
        reaindeks = 0
        for j in range(veerge-1, -1, -1):
            element = maatriks[i][j]
            if i == ridu-1:
                reajärjend = []
                reajärjend.append(element)
                Tmaatriks.append(reajärjend)
            else:
                Tmaatriks[reaindeks].append(element)
                reaindeks += 1
    return Tmaatriks
 