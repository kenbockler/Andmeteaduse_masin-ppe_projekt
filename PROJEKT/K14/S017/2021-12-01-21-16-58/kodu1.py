def rek_abs(j�rjend):
    uusj�rjend = []
    if j�rjend == []:
        return uusj�rjend
    else:
        for el in j�rjend:
            if isinstance(el, list) is False:
                uusj�rjend.append(abs(el))
            else:
                uusj�rjend.append(rek_abs(el))
        return uusj�rjend
