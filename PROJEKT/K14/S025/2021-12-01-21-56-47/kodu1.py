def rek_abs(j�r):
    uus = []
    for el in j�r:
        if isinstance(el, list):
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
    return uus