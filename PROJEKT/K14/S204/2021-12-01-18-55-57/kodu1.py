def rek_abs(j,t=[]):
    for el in j:
        if isinstance(el, list):
            t.append(rek_abs(el, []))
        else:
            new_el=abs(el)
            t.append(new_el)
    return t