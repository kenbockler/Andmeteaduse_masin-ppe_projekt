def rek_abs(j�r,mag=[]):
    for i in j�r:
        if isinstance(i, list) == True:
            mag.append(rek_abs(i,[]))
        else:
            mag.append(abs(i))
    return mag