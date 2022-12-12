def rek_abs(järjend):
    if järjend == []:
        return[]
    elif type(järjend) != list:
        järjend = abs(järjend)
        return järjend
    else:
        uus = []
        for el in järjend:
            uus.append(rek_abs(el))
        return uus
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))