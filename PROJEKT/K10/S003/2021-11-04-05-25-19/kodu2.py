def v�itja(maatriks):
    j�rjend = []
    s�nastik = {"O":0, "X":0}
    for i in range(4):
        for j in range(2):
            j�rjend.append(maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2])
    for i in range(2):
        for j in range(4):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j])
    for i in range(1):
        for j in range(1):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
    for i in range(1):
        for j in range(1):
            j�rjend.append(maatriks[i+1][j+1]+maatriks[i+2][j+2]+maatriks[i+3][j+3])
    for i in range(1):
        for j in range(3,2,-1):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j-1]+maatriks[i+2][j-2])
    for i in range(1):
        for j in range(3,2,-1):
            j�rjend.append(maatriks[i+1][j-1]+maatriks[i+2][j-2]+maatriks[i+3][j-3])
    for i in range(1):
        for j in range(1,2):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
    for i in range(1,2):
        for j in range(1):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
    for i in range(1):
        for j in range(2,1,-1):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j-1]+maatriks[i+2][j-2])
    for i in range(1,2):
        for j in range(3,2,-1):
            j�rjend.append(maatriks[i][j]+maatriks[i+1][j-1]+maatriks[i+2][j-2])
    for el in j�rjend:
        if el == "XXX":
            s�nastik["X"] += 1
        if el == "OOO" :
            s�nastik["O"] += 1
    return s�nastik
