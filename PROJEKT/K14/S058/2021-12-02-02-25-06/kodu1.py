def rek_abs(m):
    for element in m:
        if isinstance(element, list):
            rek_abs(element)
        else:
            abs(element)
    return m
m = [-2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
rek_abs(m)
print(rek_abs(m))