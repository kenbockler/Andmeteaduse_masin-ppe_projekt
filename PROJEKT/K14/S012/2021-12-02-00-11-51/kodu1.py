def rek_abs(j�rjend):
    uus_j�rjend = []
    for element in j�rjend:
        if isinstance(element, list):
            uus_j�rjend.append(rek_abs(element))
        else:
            uus_j�rjend.append(abs(element))
    return uus_j�rjend
