def j�rjesta_punktid(j�rjend):
    n = len(j�rjend)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if j�rjend [j][1] > j�rjend[j+1][1]:
                j�rjend[j], j�rjend[j+1] = j�rjend[j+1], j�rjend[j]
            if j�rjend[j][1] == j�rjend[j+1][1] and j�rjend [j][0] > j�rjend[j+1][0]:
                j�rjend[j], j�rjend[j+1] = j�rjend[j+1], j�rjend[j]
j�rjend = [(8,1), (8,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
