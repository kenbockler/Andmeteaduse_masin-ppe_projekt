def rek_abs(j�r):
    uus_j�r = []
    for el in j�r:
        if isinstance(el, list) == True:
            uus_j�r.append(rek_abs(el))
        else:
            uus_j�r.append(abs(el))
    return uus_j�r
    