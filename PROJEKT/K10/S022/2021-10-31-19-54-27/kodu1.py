def erinevad_s�mbolid(a):
    sumbolid = set()
    for sumbol in a:
        if sumbol not in sumbolid:
            sumbolid.add(sumbol)
    return sumbolid
def s�mbolite_sagedus(a):
    sagedus = {}
    for sumbol in a:
        sagedus[sumbol] = sagedus.get(sumbol, 0) + 1
    return sagedus
def grupeeri(a):
    tais = set()
    kaas = set()
    sumb = set()
    koond = {}
    sagedus = s�mbolite_sagedus(a)
    sagedus1 = list(sagedus.keys())
    for sumbol in sagedus1:
        if sumbol.lower() in "aeiou����":
            esimene = sumbol 
            teine = sagedus[sumbol]
            kolmas = (esimene, teine)
            tais.add(kolmas)
        if sumbol.lower() in "qwrtypsdfghjklmnbvcxz":
            esimene = sumbol
            teine = sagedus[sumbol]
            kolmas = (esimene, teine)
            kaas.add(kolmas)
        if sumbol.lower() not in "aeiou����qwrtypsdfghjklmnbvcxz":
            esimene = sumbol
            teine = sagedus[sumbol]
            kolmas = (esimene, teine)
            sumb.add(kolmas)
    koond["T�ish��likud"] = tais
    koond['Kaash��likud'] = kaas
    koond['Muud'] = sumb
    return koond
grupeeri("s�ida tasa �le silla")