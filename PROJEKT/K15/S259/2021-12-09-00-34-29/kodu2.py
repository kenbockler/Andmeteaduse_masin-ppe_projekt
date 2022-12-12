def järjesta_punktid(punktid):
    for i in range(len(punktid)):
        for j in range(len(punktid)-1):
            if punktid[j][1] > punktid[j+1][1]:
                punktid[j], punktid[j+1] = punktid[j+1], punktid[j]
            elif punktid[j][1] == punktid[j+1][1]:
                if punktid[j][0] > punktid[j+1][0]:
                    punktid[j], punktid[j+1] = punktid[j+1], punktid[j]
    print(punktid)