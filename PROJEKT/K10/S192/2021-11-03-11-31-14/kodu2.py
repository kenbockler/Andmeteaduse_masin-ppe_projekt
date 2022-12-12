def võitja(maatriks):
    punktid = {}
    O = uuri('O', maatriks)
    X = uuri('X', maatriks)
    punktid['O'] = O
    punktid['X'] = X
    return punktid
def uuri(sümbol, maatriks):
    esinemise_arv = 0
    korda_3 = sümbol*3
    for i in range(4):
        for j in range(2):
            summa = maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if korda_3 == summa:
                esinemise_arv += 1
    for i in range(2):
        for j in range(4):
            summa = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if korda_3 == summa:
                esinemise_arv += 1
    for i in range(2):
        for j in range(2):
            summa = maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            if korda_3 == summa:
                esinemise_arv += 1
    for i in range(2):
        for j in range(2):
            summa = maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]
            if korda_3 == summa:
                esinemise_arv += 1
    return esinemise_arv