def rek_abs(järjend):
    uus=[]
    for el in järjend:
        if isinstance(el, list)==True:
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
    return uus