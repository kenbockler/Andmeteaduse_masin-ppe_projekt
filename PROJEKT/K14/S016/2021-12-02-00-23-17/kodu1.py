def rek_abs(j�rjend):
    x = []
    for el in j�rjend:
        if isinstance(el, list):
            y = rek_abs(el)
            x.append(y)
        else:
            x.append(abs(el))
    return x
print(rek_abs([-2, 6, [-3]]))