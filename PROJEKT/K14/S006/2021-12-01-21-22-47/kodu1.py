def rek_abs(järjend):
    uus = []
    if järjend == []:
        return uus
    else:
        for element in järjend:
            if not isinstance(element, list):
                uus.append(abs(element))
            else:
                uus.append(rek_abs(element))
    return uus