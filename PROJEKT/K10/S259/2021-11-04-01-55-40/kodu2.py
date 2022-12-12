def võitudearv(m, sümbol):
    kokku = 0
    for i in range(len(m)):
        for j in range(len(m[i])-2):
            if m[i][j] == m[i][j+1] == m[i][j+2] == sümbol:
                kokku += 1
    for i in range(len(m)-2):
        for j in range(len(m[i])):
            if m[i][j] == m[i+1][j] == m[i+2][j] == sümbol:
                kokku += 1
    for i in range(len(m)-2):
        for j in range(len(m[i])-2):
            if m[i][j] == m[i+1][j+1] == m[i+2][j+2] == sümbol:
                kokku += 1
    for i in range(len(m)-2):
        for j in range(len(m[i])-2):
            if m[i][j] == m[i+1][j-1] == m[i+2][j-2] == sümbol:
                kokku += 1
    return kokku
def võitja(m):
    võite_O = võitudearv(m,'O')
    võite_X = võitudearv(m, 'X')
    return {'O': võite_O, 'X': võite_X}
