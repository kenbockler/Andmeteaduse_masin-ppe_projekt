p = [(1, 2), (2, 1)]
def kontroll(p):
    pikkus = len(p)
    lugeja = 0
    for i in range(0, pikkus - 1):
        if p[i][1] == p[i+1][1]:
            lugeja += 1
    if lugeja == pikkus - 1:
        return True
def järjesta_punktid(p):
    if kontroll(p) == True:
        for i in range(len(p)):
            min = i
            for j in range(i+1, len(p)):
                if p[j][0] < p[min][0]:
                    min = j
            if i != min:
                p[i], p[min] = p[min], p[i]
    else:
        for i in range(len(p)):
            min = i
            for j in range(i+1, len(p)):
                if p[j][1] < p[min][1]:
                    min = j
            if i != min:
                p[i], p[min] = p[min], p[i]
järjesta_punktid(p)
print(p)