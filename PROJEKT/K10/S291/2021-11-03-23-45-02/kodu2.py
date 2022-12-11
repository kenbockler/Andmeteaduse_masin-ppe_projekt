def võitja(maatriks):
    sõnastik = {}
    X_loendur = 0
    O_loendur = 0
    for i in range(len(maatriks)):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "X":
                X_loendur += 1
            elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                O_loendur += 1
    for i in range(2):
        for j in range(len(maatriks)):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
                X_loendur += 1
            elif maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                X_loendur += 1
            elif maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "X":
                X_loendur += 1
            elif maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "O":
                O_loendur += 1
    sõnastik["O"] = O_loendur
    sõnastik["X"] = X_loendur
    return sõnastik
print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))