def erinevad_sümbolid(sõne):
    j = list(sõne)
    return set(j)
def sümbolite_sagedus(sõne):
    j = list(sõne)
    d = {}
    for el in j:
        d[el] = d.get(el, 0)+1
    return d
def grupeeri(sõne):
    vokaalid = tuple('aeiouõäöü') + tuple(('aeiouõäöü').upper())
    konsonandid = tuple('qwrtypsdfghjklzxcvbnm') + tuple(('qwrtypsdfghjklzxcvbnm').upper())
    sõn = set(sõne)
    sõnastik = {}
    v =  set()
    k = set()
    m = set()
    for el in sõn:
        if el not in vokaalid:
            if el not in konsonandid:
                i = sõne.count(el)
                m.add((el, i))
        if el in vokaalid:
            i = sõne.count(el)
            v.add((el, i))
        if el in konsonandid:
            i = sõne.count(el)
            k.add((el, i))
    sõnastik['Täishäälikud'] = v        
    sõnastik['Kaashäälikud'] = k
    sõnastik['Muud'] = m
    return sõnastik
print(grupeeri("abcdefghijklmnopqrstuvwxyz"))