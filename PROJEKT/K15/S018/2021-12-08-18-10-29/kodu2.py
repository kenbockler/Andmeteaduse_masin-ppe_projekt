def j�rjesta_punktid(j�r):
    n = len(j�r)
    for i in range(n-1):
        for j in range(n-i-1):
            if j�r[j][1] > j�r[j+1][1]:
                j�r[j], j�r[j+1] = j�r[j+1], j�r[j]
            elif j�r[j][1] == j�r[j+1][1]:
                if j�r[j][0] > j�r[j+1][0]:
                    j�r[j], j�r[j+1] = j�r[j+1], j�r[j]
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
j�rjesta_punktid(p)