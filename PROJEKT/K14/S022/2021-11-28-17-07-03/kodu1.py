def rek_abs(a):
    list1 = []
    if isinstance(a, list) == False:
        return abs(a)
    if isinstance(a, list) == True:
        for b in a:
            list1.append(rek_abs(b))
        return list1