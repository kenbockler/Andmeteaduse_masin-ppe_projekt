def transponeeriK(m):
    t = []
    for i in range(len(m[0])-1, -1, -1):
        list = []
        for j in range(len(m)-1, -1, -1):
            list.append(m[j][i])
        t.append(list)
    return t