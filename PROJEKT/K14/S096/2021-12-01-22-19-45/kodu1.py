def rek_abs(järjend):
    uus_järjend = []
    if len(järjend) == 0:
        return uus_järjend
    else:
        for i in järjend:
            if isinstance(i, list):
                uus_järjend.append(rek_abs(i))
            else:
                uus_järjend.append(abs(i))
        return uus_järjend
l = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
print(rek_abs(l))