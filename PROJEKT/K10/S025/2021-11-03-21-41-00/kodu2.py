def v�itja(j�r):
    d = {}
    xid = 0
    od = 0
    for i in range(4):
        for j in range(2):
            if j�r[i][j] == j�r[i][j+1] == j�r[i][j+2]:
                if j�r[i][j] == 'X':
                    xid += 1
                if j�r[i][j] == 'O':
                    od += 1
    for i in range(2):
        for j in range(4):
            if j�r[i][j] == j�r[i+1][j] == j�r[i+2][j]:
                if j�r[i][j] == 'X':
                    xid += 1
                if j�r[i][j] == 'O':
                    od += 1
    for i in range(2):
        for j in range(2):
            if j�r[i][j] == j�r[i+1][j+1] == j�r[i+2][j+2]:
                if j�r[i][j] == 'X':
                    xid += 1
                if j�r[i][j] == 'O':
                    od += 1
    for i in range(2):
        for j in range(2):
            if j�r[i][j+2] == j�r[i+1][j+1] == j�r[i+2][j]:
                if j�r[i][j+2] == 'X':
                    xid += 1
                if j�r[i][j+2] == 'O':
                    od += 1              
    d['O'] = od
    d['X'] = xid
    return d