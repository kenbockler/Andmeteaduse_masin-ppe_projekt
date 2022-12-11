def võitja(maatriks):
    seis = {'O' : 0, 'X' : 0}
    for i in range(4):
        rida = maatriks[i]
        for j in range(4):
            el = rida[j]
            t1 = j + 2
            t2 = i + 2
            t3 = j - 2
            if el in seis:
                if t1 < 4:
                    if rida[j+1] == el and rida[j+2] == el:
                        seis[el] += 1
                if t2 < 4:
                    if maatriks[i+1][j] == el and maatriks[i+2][j] == el:
                        seis[el] += 1
                if t1 < 4 and t2 < 4:
                    if maatriks[i+1][j+1] == el and maatriks[i+2][j+2] == el:
                        seis[el] += 1
                if t2 < 4 and t3 >= 0:
                    if maatriks[i+1][j-1] == el and maatriks[i+2][j-2] == el:
                        seis[el] += 1
    return seis
