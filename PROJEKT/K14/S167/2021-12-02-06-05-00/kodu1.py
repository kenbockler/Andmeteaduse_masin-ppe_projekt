jar = [1, [-2], 3]
def rek_abs(jar):
    t = []
    for i in range(0, len(jar)):
        d = jar[i]
        if isinstance(d, list) == False:
            t.append(abs(d))
        if isinstance(d, list) == True:
            t.append(rek_abs(d))
    return t
print(rek_abs(jar))