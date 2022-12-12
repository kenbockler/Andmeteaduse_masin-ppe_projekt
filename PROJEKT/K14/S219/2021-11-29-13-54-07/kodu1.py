def rek_abs(järjend):
    abilist = []
    for arv in järjend:
        if isinstance(arv, list):
            abilist.append(rek_abs(arv))
        else:
            abilist.append(abs(arv))
    return abilist