def rek_abs(järjend):
    järjend_abs = []
    for el in järjend:
        if isinstance(el, list) == 1:
            järjend_abs.append(rek_abs(el))
        else:
            järjend_abs.append(abs(el))
    return järjend_abs
