def v�itja(maatriks):
    X_loendur = 0
    O_loendur = 0
    s�nastik = {}
    for i in range(4):
        for j in range(2):
            el = maatriks[i][j]
            if el == "X":
                if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=="X":
                    X_loendur += 1
            if el == "O":
                if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=="O":
                    O_loendur += 1
    for i in range(2):
        for j in range(4):
            el = maatriks[i][j]
            if el == "X":
                if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=="X":
                    X_loendur += 1
            if el == "O":
                if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=="O":
                    O_loendur += 1
        for j in range(2):
            el = maatriks[i][j]
            if el == "X":
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=="X":
                    X_loendur += 1
            if el == "O":
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=="O":
                    O_loendur += 1
        for j in range(2,4):
            el = maatriks[i][j]
            if el == "X":
                if maatriks[i][j]==maatriks[i+1][j-1]==maatriks[i+2][j-2]=="X":
                    X_loendur += 1
            if el == "O":
                if maatriks[i][j]==maatriks[i+1][j-1]==maatriks[i+2][j-2]=="O":
                    O_loendur += 1
    s�nastik["O"] = O_loendur
    s�nastik["X"] = X_loendur
    return s�nastik
