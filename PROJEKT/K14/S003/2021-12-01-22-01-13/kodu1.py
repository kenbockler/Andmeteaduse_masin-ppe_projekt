def rek_abs(j�rjend):
    v��rtused = []
    for el in j�rjend:
        if isinstance(el,list) == False:
            v��rtused.append(abs(el))
        else:
            v��rtused.append(rek_abs(el))
    return v��rtused
