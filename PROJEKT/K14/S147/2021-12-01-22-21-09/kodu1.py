def rek_abs(järjend,väljund=list(),sügavus=0):
    ajutine = list()
    for el in järjend:
        if isinstance(el, list):
            rek_abs(el,väljund,sügavus+1)
        elif sügavus > 0:
            ajutine.append(abs(el))
        else:
            väljund.append(abs(el))
    if sügavus > 0:
        väljund.append(ajutine)
    return väljund
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))