def v�itja(maatriks):
    X_loendur = 0
    O_loendur = 0
    for i in range(4):
        for j in range(2):
            s�mbol = (maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2])
            if s�mbol == "XXX":
                X_loendur += 1
            if s�mbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(4):
            s�mbol=(maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j])
            if s�mbol == "XXX":
                X_loendur += 1
            if s�mbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            s�mbol = (maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
            if s�mbol == "XXX":
                X_loendur += 1
            if s�mbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            s�mbol = (maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j])
            if s�mbol == "XXX":
                X_loendur += 1
            if s�mbol == "OOO":
                O_loendur += 1
    andmed = {"O":O_loendur, "X": X_loendur}
    return andmed