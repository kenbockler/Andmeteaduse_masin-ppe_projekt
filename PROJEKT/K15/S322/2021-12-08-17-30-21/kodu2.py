def järjesta_punktid(p):
    for k in range(2):
        sorteeritud = False
        while not sorteeritud:
            for i in range(len(p)-1):
                backup = p[i+1]
                if p[i][k] > p[i+1][k]:
                    p[i+1] = p[i]
                    p[i] = backup
            sorteeritud = True
            for i in range(len(p)-1):
                if p[i][k] > p[i+1][k]:
                    sorteeritud = False
                    break
