def rek_abs(jrnd):
    if jrnd == []:
        return []
    else:
        if isinstance(jrnd[0], list):
            return [rek_abs(jrnd[0])] + rek_abs(jrnd[1:])
        else:
            if jrnd[0] > 0:
                return [jrnd[0]] + rek_abs(jrnd[1:])
            else:
                return [-jrnd[0]] + rek_abs(jrnd[1:])
