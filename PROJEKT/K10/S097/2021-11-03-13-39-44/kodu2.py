def võitja(maatriks):
    O3 = 0
    X3 = 0
    for i in range(len(maatriks)):
        for j in range(2):
            if maatriks[i][j] == " ":
                continue
            elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]:
                if maatriks[i][j] == "O":
                    O3 += 1
                elif maatriks[i][j] == "X":
                    X3 += 1
            else:
                continue
    for i in range(2):
        for j in range(len(maatriks)):
            if maatriks[i][j] == " ":
                continue
            elif maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]:
                if maatriks[i][j] == "O":
                    O3 += 1
                elif maatriks[i][j] == "X":
                    X3 += 1
            else:
                continue
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == " ":
                continue
            elif maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2]:
                if maatriks[i][j] == "O":
                    O3 += 1
                elif maatriks[i][j] == "X":
                    X3 += 1
            else:
                continue
    for i in range(2):
        for j in range(2,4):
            if maatriks[i][j] == " ":
                continue
            elif maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2]:
                if maatriks[i][j] == "O":
                    O3 += 1
                elif maatriks[i][j] == "X":
                    X3 += 1
            else:
                continue
    sõnastik = {}
    sõnastik["O"] = O3
    sõnastik["X"] = X3
    return sõnastik
