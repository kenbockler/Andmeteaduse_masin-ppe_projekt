def võitja(a):
    sõnastik = {'X': 0, 'O': 0}
    for x in range (4):
        for j in range (4):
            if a[x][j] == 'X':
                if x+2 < 4:
                    if a[x+1][j] == 'X' and a[x+2][j] == 'X':
                        sõnastik['X'] += 1
                if j+2 < 4:
                    if a[x][j+1] == 'X' and a[x][j+2] == 'X':
                        sõnastik['X'] += 1
                if x+2 < 4 and j+2 < 4:
                    if a[x+1][j+1] == 'X' and a[x+2][j+2] == 'X':
                        sõnastik['X'] += 1
                if x-2 > -1 and j+2 < 4:
                    if a[x-1][j+1] == 'X' and a[x-2][j+2] == 'X':
                        sõnastik['X'] += 1
            if a[x][j] == 'O':
                if x+2 < 4:
                    if a[x+1][j] == 'O' and a[x+2][j] == 'O':
                        sõnastik['O'] += 1
                if j+2 < 4:
                    if a[x][j+1] == 'O' and a[x][j+2] == 'O':
                        sõnastik['O'] += 1
                if x+2 < 4 and j+2 < 4:
                    if a[x+1][j+1] == 'O' and a[x+2][j+2] == 'O':
                        sõnastik['O'] += 1
                if x-2 > -1 and j+2 < 4:
                    if a[x-1][j+1] == 'O' and a[x-2][j+2] == 'O':
                        sõnastik['O'] += 1
    return(sõnastik)
