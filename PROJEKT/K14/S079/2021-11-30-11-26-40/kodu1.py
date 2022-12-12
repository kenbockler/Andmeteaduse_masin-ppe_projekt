def rek_abs(järjend):
    if type(järjend) != list:
        return abs(järjend)
    else:
        if järjend == []:
            return []
        else:
            järjend1 = []
            for element in järjend:
                elemendid = rek_abs(element)
                järjend1.append(elemendid)
            return(järjend1)