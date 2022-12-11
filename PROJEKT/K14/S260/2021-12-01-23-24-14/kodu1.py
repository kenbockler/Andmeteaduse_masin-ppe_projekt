def rek_abs(l):
    uus_järjend = []
    for i in range(len(l)):
        if isinstance(l[i],list):
            uus_järjend.append(rek_abs(l[i]))
            i += 1
            if i == len(l):
                return uus_järjend
        try:
            uus_järjend.append(abs(l[i]))
        except:
            pass
    return uus_järjend
print(rek_abs([1, -3, 20, [-10, -5], []]))