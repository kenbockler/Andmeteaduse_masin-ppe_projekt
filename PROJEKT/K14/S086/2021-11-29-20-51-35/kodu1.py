def rek_abs(sisend):
    if isinstance(sisend, (int, float)):
        return abs(sisend)
    elif isinstance(sisend, (list, tuple)):
        väljund = []
        for element in sisend:
            väljund.append(rek_abs(element))
        return väljund
    