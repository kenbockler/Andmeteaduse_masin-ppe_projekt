def erinevad_s�mbolid(s):
    return set(s)
def s�mbolite_sagedus(s):
    j�r = list(s)
    d = {}
    for a in j�r:
        d[a] = d.get(a, 0) + 1
    return d
def grupeeri(s):
    t�is = list('aeiou����AEIOU����')
    kaas = list('bcdfghjklmnpqrs�z�tvwxyBCDFGHJKLMNPQRS�Z�TVWXY')
    s�nej�r = list(s)
    d = {}
    d['T�ish��likud'] = set()
    d['Kaash��likud'] = set()
    d['Muud'] = set()
    b = s�mbolite_sagedus(s)
    for a in b:
        if a in t�is:
            d['T�ish��likud'].add((a, b[a]))
        elif a in kaas:
            d['Kaash��likud'].add((a, b[a]))
        else:
            d['Muud'].add((a, b[a]))
    return d
print(grupeeri("s�ida tasa �le silla"))