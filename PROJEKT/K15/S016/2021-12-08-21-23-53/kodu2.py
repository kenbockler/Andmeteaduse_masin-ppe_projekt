p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def j�rjesta_punktid(j�rjend):
    t�hi = []
    pikkus = len(j�rjend)-1
    i = 0
    for j in range(pikkus):
        for i in range(pikkus):
            if j�rjend[i][1] > j�rjend[i+1][1]:
                j�rjend[i], j�rjend[i+1] = j�rjend[i+1], j�rjend[i]
                if i == 5:
                    t�hi.append(j�rjend)
            elif j�rjend[i][1] == j�rjend[i+1][1]:
                j�rjend[i], j�rjend[i+1] = j�rjend[i], j�rjend[i+1]
                if i == 5:
                    t�hi.append(str(j�rjend))
    print(t�hi)
j�rjesta_punktid(p)