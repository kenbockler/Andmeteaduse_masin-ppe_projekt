def rek_abs(järjend):
    if len(järjend) == 0:
        return []
    else:
        esimene = järjend[0]
        jääk = järjend[1:]
        läbi = rek_abs(jääk)
        if isinstance(esimene,list):
            return [rek_abs(esimene)] + läbi
        else:
            return [abs(esimene)] + läbi