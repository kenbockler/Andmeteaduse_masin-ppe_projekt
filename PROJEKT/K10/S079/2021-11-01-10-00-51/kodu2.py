def võitja(m):
    O_read = 0
    X_read = 0
    for i in range(4):
        for j in range(2):
            if m[i][j] == m[i][j+1] == m[i][j+2] == "O":
                O_read += 1
            elif m[i][j] == m[i][j+1] == m[i][j+2] == "X":
                X_read += 1
    O_veerud = 0
    X_veerud = 0
    for i in range(2):
        for j in range(4):
            if m[i][j] == m[i+1][j] == m[i+2][j] == "O":
                O_veerud += 1
            elif m[i][j] == m[i+1][j] == m[i+2][j] == "X":
                X_veerud += 1
    O_pd1 = 0
    X_pd1 = 0
    for i in range(2):
        for j in range(2):
            if m[i][j] == m[i+1][j+1] == m[i+2][j+2] == "O":
                O_pd1 += 1
            elif m[i][j] == m[i+1][j+1] == m[i+2][j+2] == "X":
                X_pd1 += 1
    O_pd2 = 0
    X_pd2 = 0
    for i in range(2):
        for j in range(2,0,-1):
            if m[i][j+1] == m[i+1][j] == m[i+2][j-1] == "O":
                O_pd2 += 1
            elif m[i][j+1] == m[i+1][j] == m[i+2][j-1] == "X":
                X_pd2 += 1
    O_kokku = O_read + O_veerud + O_pd1 + O_pd2
    X_kokku = X_read + X_veerud + X_pd1 + X_pd2
    d = {'O' : O_kokku, 'X' : X_kokku}
    return d
    