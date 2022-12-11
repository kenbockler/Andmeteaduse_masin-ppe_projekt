def järjesta_punktid(koordinaadid):
    for i in range(len(koordinaadid)):
        for j in range(len(koordinaadid)):
            if koordinaadid[i][1] < koordinaadid[j][1]:
                koordinaadid[i], koordinaadid[j] = koordinaadid[j], koordinaadid[i]
            elif koordinaadid[i][1] == koordinaadid[j][1]:
                if koordinaadid[i][0] < koordinaadid[j][0]:
                    koordinaadid[i], koordinaadid[j] = koordinaadid[j], koordinaadid[i]