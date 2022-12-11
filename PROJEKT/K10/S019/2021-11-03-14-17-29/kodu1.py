def erinevad_s�mbolid(s�ne):
    return set(s�ne)
def s�mbolite_sagedus(s�ne):
    d = {}
    for arv in s�ne:
        d[arv] = d.get(arv, 0) + 1
    return d
def grupeeri(s�ne):
    t�ish��likud = {"a","e","i","o","u","�","�","�","�"}
    kaash��likud = {"q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","�","�","x","c","v","b","n","m"}
    muu = set(s�ne) - (t�ish��likud|kaash��likud)
    s�mbolite_sagedus(s�ne)
    tn = set()
    kn = set()
    mn = set()
    for ib in s�ne:
        bn = (ib, s�mbolite_sagedus(s�ne)[ib])
        if ib in t�ish��likud:
           tn.add(bn)
        elif ib in kaash��likud:
            kn.add(bn)
        elif ib in muu:
            mn.add(bn)
    an = {'T�ish��likud': tn, 'Kaash��likud': kn, 'Muud': mn}
    return an
    