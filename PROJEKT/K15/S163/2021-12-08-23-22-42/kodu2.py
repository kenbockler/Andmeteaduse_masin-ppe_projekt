p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(p):
    while True:
        swap = False
        for i in range(len(p)-1):
            if p[i][1] > p[i+1][1]:
                swap = True
                el1 = p[i]
                el2 = p[i+1]
                p[i+1] = el1
                p[i] = el2
            elif p[i][1] == p[i+1][1]:
                if p[i][0] > p[i+1][0]:
                    swap = True
                    el1 = p[i]
                    el2 = p[i+1]
                    p[i+1] = el1
                    p[i] = el2  
        if swap == False:
            break
järjesta_punktid(p) 
print(p)