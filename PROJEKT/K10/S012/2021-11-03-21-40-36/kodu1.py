def erinevad_s�mbolid(x):
    return set(x)
def s�mbolite_sagedus(x):
    kordused = {}
    for i in x:
        kordused[i] = kordused.get(i, 0) + 1
    return kordused
def grupeeri(x):
    th = {"a", "e", "i", "o", "u", "�", "�", "�", "�"}
    kh = {"h", "j", "l", "m", "n", "r", "s", "v", "k", "p", "t", "g", "b", "d"}
    t�ish��likud = {}
    kaash��likud = {}
    muud = {}
    for i in x:
        if i in th:
            t�ish��likud[i] = t�ish��likud.get(i, 0)+1
        elif i in kh:
            kaash��likud[i] = kaash��likud.get(i, 0)+1
        else:
            muud[i] = muud.get(i, 0)+1
    grupeering = {
                "T�ish��likud" : t�ish��likud, 
                "Kaash��likud" : kaash��likud,
                "Muud" : muud}
    return grupeering
    