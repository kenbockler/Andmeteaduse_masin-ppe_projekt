p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(punktid):
    for i in range(len(punktid)):
        for j in range(i+1, len(punktid)):
            if punktid[i][1] > punktid[j][1]:
                punktid[i], punktid[j] = punktid[j], punktid[i]
    for i in range(len(punktid)):
        for j in range(i+1, len(punktid)):
            if punktid[i][1] == punktid[j][1] and punktid[i][0] > punktid[j][0]:
                punktid[i], punktid[j] = punktid[j], punktid[i]
järjesta_punktid(p)
        