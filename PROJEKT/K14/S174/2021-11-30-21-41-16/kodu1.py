def rek_abs(jär):
    jär_abs = []
    for el in jär:
        if isinstance(el, list) == 1:
            jär_abs.append(rek_abs(el))
        else:
            jär_abs.append(abs(el))
    return jär_abs