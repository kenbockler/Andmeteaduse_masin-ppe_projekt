def rek_abs(järjend):
    uus_järjend = []
    if järjend == []:
        return uus_järjend
    for el in range(len(järjend)):
        try:
            if järjend[el] < 0:
                uus_järjend.append(-(järjend[el]))
            else:
                uus_järjend.append(järjend[el])
        except:
            uus_järjend.append(rek_abs(järjend[el]))
    return uus_järjend