p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(p):
    järjendi_pikkus = len(p)
    for i in range(0, järjendi_pikkus):
        for j in range(0, järjendi_pikkus-i-1):
            if (p[j][1] > p[j + 1][1]):
                uus_p = p[j]
                p[j] = p[j + 1]
                p[j + 1] = uus_p
    print(p)
järjesta_punktid(p)