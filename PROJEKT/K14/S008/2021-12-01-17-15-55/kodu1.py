def rek_abs(j�rjend):
    uus =[]
    for el in j�rjend:
        if isinstance(el, list):
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
    return uus
print (rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))