def erinevad_sümbolid(tekst):
    return set(tekst)
def sümbolite_sagedus(tekst):
    hulk = erinevad_sümbolid(tekst)
    d = {}
    for el in hulk:
        d[el] = tekst.count(el)
    return d
def grupeeri(tekst):
    sümbolid = sümbolite_sagedus(tekst)
    v = set()
    k = set()
    m = set()
    for sümbol in sümbolid:
        if sümbol in 'aeiouõäöüAEIOUÕÄÖÜ':
            v.add((sümbol, sümbolid[sümbol]))
        elif sümbol in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy':
            k.add((sümbol, sümbolid[sümbol]))
        else:
            m.add((sümbol, sümbolid[sümbol]))
    grupid = {}
    grupid['Täishäälikud'] = v
    grupid['Kaashäälikud'] = k
    grupid['Muud'] = m
    return grupid
