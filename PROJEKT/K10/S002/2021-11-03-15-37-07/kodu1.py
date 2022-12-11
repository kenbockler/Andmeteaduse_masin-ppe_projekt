def erinevad_s�mbolid(tekst):
    return set(tekst)
def s�mbolite_sagedus(tekst):
    d = dict.fromkeys(erinevad_s�mbolid(tekst), 0)
    for i in tekst:
        if i in d:
            d[i] += 1
    return d
def grupeeri(tekst):
    d = {"T�ish��likud": set(),
         "Kaash��likud": set(),
         "Muud": set()}
    a = s�mbolite_sagedus(tekst)
    for i in a:
        if i in "i�ue��o�aI�UE��O�A":
            d["T�ish��likud"].add((i,a[i]))
        elif i in "bcdfghjklmnpqrs�z�tvwxyBCDFGHJKLMNPQRS�Z�TVWXY":
            d["Kaash��likud"].add((i,a[i]))
        else:
            d["Muud"].add((i,a[i]))
    return d