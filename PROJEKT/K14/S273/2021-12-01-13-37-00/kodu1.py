def rek_abs(järjend):
    for n in järjend:
        if isinstance(n, list) == False:
            järjend[järjend.index(n)] = abs(n)
        if isinstance(n, list) == True:
            rek_abs(järjend[järjend.index(n)])
    return järjend