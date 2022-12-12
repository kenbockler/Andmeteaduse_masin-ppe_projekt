def rek_abs(j):
    uus_j = []
    if j == []:
        return []
    if isinstance(j, list):
        for el in j:
            uus_j.append(rek_abs(el))            
        return uus_j
    else:
        return abs(j)
