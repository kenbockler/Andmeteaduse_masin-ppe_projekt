def rek_abs(j�rjend):
    uus = []
    if j�rjend == []:
        return uus
    else:
        for element in j�rjend:
            if not isinstance(element, list):
                uus.append(abs(element))
            else:
                uus.append(rek_abs(element))
    return uus