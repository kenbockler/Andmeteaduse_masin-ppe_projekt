def rek_abs(j�rjend):
    uus_j�rjend = []
    for el in j�rjend:
        if isinstance(el, list):
            uus_j�rjend.append(rek_abs(el))
        else:
            uus_j�rjend.append(abs(el))
    return uus_j�rjend
print(rek_abs([]))