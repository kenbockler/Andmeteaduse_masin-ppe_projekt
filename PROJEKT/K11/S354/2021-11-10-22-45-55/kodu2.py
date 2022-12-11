import copy
def transponeeriK(a):
    b = copy.deepcopy(a)
    for r in range(len(a)):
        a[r] = b[(len(a)-(r+1))]
    d = []
    dd = [] 
    for n in range(len(a[0])):
        dd = []
        for i in range(len(a)):
            dd += [a[i][n]]
        d += [dd]
    c =copy.deepcopy(d)
    for r in range(len(d)):
        d[r] = c[(len(d)-(r+1))]
    return d
