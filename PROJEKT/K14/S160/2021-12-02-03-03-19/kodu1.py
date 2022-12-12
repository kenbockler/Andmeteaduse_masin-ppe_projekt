def rek_abs(järjend1):
    järjend2 = []
    for i in järjend1:
        if isinstance(i, list):
            järjend2.append(rek_abs(i))
        else:                             
            järjend2.append(abs(i))
    return järjend2
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))