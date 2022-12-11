def järjesta_punktid(p):
    for i in range(len(p)):
        min = i
        for j in range(i+1, len(p)):
            if p[j][1] < p[min][1]:
                min = j
        if i != min:
            p[i], p[min] = p[min], p[i]
    for i in range(len(p)):
        min=i
        for j in range(i+1, len(p)):
            if p[j][1]!= p[min][1]:
                pass
            elif p[i][1]== p[i+1][1]:
                if p[min][0]> p[j][0]:
                    min= j
        if i != min:
                p[i], p[min] = p[min], p[i]
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
v= järjesta_punktid(p)
print(p)