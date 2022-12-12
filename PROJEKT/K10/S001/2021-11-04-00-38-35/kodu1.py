def erinevad_s�mbolid(sone):
    return set(sone)
def s�mbolite_sagedus(sone):
    sonastik = {}
    for symbol in erinevad_s�mbolid(sone):
        sonastik[symbol] = sone.count(symbol)
    return sonastik
def grupeeri(sone):
    sonastik = s�mbolite_sagedus(sone)
    tais = set()
    kaas = set()
    muud = set()
    for voti in sonastik:
        if voti in "aeuio����AEUIO����":
            tais.add((voti,sonastik[voti]))
        elif voti in "qwrtypsdfghjklzxcvbnm��QWRTYPSDFGHJKLZXCVBNM��":
            kaas.add((voti,sonastik[voti]))
        else:
            muud.add((voti,sonastik[voti]))
    grupid = {"T�ish��likud": tais, "Kaash��likud": kaas, "Muud": muud}
    return grupid
