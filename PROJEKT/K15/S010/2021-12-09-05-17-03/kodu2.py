p = [(1, 4), (6, 4), (4, 4), (3, 4)]
def j�rjesta_punktid(p):
    for indeks in range(0, len(p)-1):
        v�him=indeks
        for j in range(indeks, len(p)):
            if p[j][1]<p[v�him][1]:
                v�him=j
            elif p[j][1]==p[v�him][1] and p[j][0]<p[v�him][0]:
                v�him=j            
        p[indeks], p[v�him]=p[v�him], p[indeks]
j�rjesta_punktid(p)
print(p)