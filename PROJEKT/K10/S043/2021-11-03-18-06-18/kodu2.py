def võitja(sisend):
    x_loendur = 0
    o_loendur = 0
    for i in range(4):
        for j in range(2):
            if sisend[i][j]+sisend[i][j+1]+sisend[i][j+2] == 'XXX':
                x_loendur += 1
            elif sisend[i][j]+sisend[i][j+1]+sisend[i][j+2] == 'OOO':
                o_loendur += 1
    for i in range(2):
        for j in range(4):
            if sisend[i][j]+sisend[i+1][j]+sisend[i+2][j] == 'XXX':
                x_loendur += 1
            elif sisend[i][j]+sisend[i+1][j]+sisend[i+2][j] == 'OOO':
                o_loendur += 1
    for i in range(2):
        for j in range(2):
            if sisend[i][j]+sisend[i+1][j+1]+sisend[i+2][j+2] == 'XXX':
                x_loendur += 1
            elif sisend[i][j]+sisend[i+1][j+1]+sisend[i+2][j+2] == 'OOO':
                o_loendur += 1
    if sisend[3][0]+sisend[2][1]+sisend[1][2] == 'XXX':
        x_loendur += 1
    if sisend[0][3]+sisend[1][2]+sisend[2][1] == 'XXX':
        x_loendur += 1
    if sisend[3][0]+sisend[2][1]+sisend[1][2] == 'OOO':
        o_loendur += 1
    if sisend[0][3]+sisend[1][2]+sisend[2][1] == 'OOO':
        o_loendur += 1
    if sisend[2][0]+sisend[1][1]+sisend[0][2] == 'XXX':
        x_loendur += 1
    if sisend[2][0]+sisend[1][1]+sisend[0][2] == 'OOO':
        o_loendur += 1
    if sisend[3][1]+sisend[2][2]+sisend[1][3] == 'XXX':
        x_loendur += 1
    if sisend[3][1]+sisend[2][2]+sisend[1][3] == 'OOO':
        o_loendur += 1
    sõn = {'X':x_loendur, 'O':o_loendur}
    return sõn
print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))