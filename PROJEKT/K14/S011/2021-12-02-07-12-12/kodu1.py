def rek_abs(j�rjend):
    uus = []
    if j�rjend == []:
        return uus
    for el in j�rjend:
        if isinstance(el, list) is True:
            uus.append(rek_abs(el))
        else:
            if el < 0:
                uus.append(-el)
            else:
                uus.append(el)
    return uus
                