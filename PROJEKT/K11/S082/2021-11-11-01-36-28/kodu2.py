def transponeeriK(m):
    vahepealne = []
    for a in range(len(m)):
        vahepealne.append(m[a])
    vahepealne.reverse()
    uus = []
    for a in range(len(vahepealne[0])):
        uus.append([])
    kordaja = 0
    a = 0
    while True:
        uus[kordaja].append(vahepealne[a][-1])
        vahepealne[a].remove(vahepealne[a][-1])
        a+=1
        if a == len(m):
            a = 0
        if len(uus[-1]) == len(m):
            break
        if len(uus[kordaja]) == len(m):
            kordaja += 1
    return(uus)
transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])