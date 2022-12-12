def võitja(m):
    d = dict()
    d["X"] = 0
    d["O"] = 0
    for i in range(4):
        for j in range(2):
            if m[i][j] == " ":
               continue
            t_üks = m[i][j]
            t_kaks = m[i][j+1]
            t_kolm = m[i][j+2]
            if t_üks == t_kaks and t_üks == t_kolm:
                d[t_üks] = d[t_üks] + 1
    for i in range(2):
        for j in range(4):
            if m[i][j] == " ":
               continue
            t_üks = m[i][j]
            t_kaks = m[i+1][j]
            t_kolm = m[i+2][j]
            if t_üks == t_kaks and t_üks == t_kolm:
                d[t_üks] = d[t_üks] + 1
    for i in range(2):
        for j in range(2):
            if m[i][j] == " ":
               continue
            t_üks = m[i][j]
            t_kaks = m[i+1][j+1]
            t_kolm = m[i+2][j+2]
            if t_üks == t_kaks and t_üks == t_kolm:
                d[t_üks] = d[t_üks] + 1
    for i in range(2):
        for j in range(2, 4):
            if m[i][j] == " ":
               continue
            t_üks = m[i][j]
            t_kaks = m[i+1][j-1]
            t_kolm = m[i+2][j-2]
            if t_üks == t_kaks and t_üks == t_kolm:
                d[t_üks] = d[t_üks] + 1
    return d
