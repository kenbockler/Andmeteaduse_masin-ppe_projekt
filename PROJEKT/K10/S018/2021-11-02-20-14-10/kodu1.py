def erinevad_s�mbolid(s�ne):
    hulk = set(s�ne)
    return hulk
def s�mbolite_sagedus(s�ne):
    s�nastik = {}
    for s�mb in s�ne:
        s�nastik[s�mb] = s�nastik.get(s�mb, 0) + 1
    return s�nastik
def grupeeri(s�ne):
    t�ish��likud = "i�ue��o�aI�UE��O�A"
    kaash��likud = "cxywqbdfghjklmnprs�z�tvCXYWQBDFGHJKLMNPRSZTV��"
    k�ik_s�mb = erinevad_s�mbolid(s�ne)
    sagedus = s�mbolite_sagedus(s�ne)
    t�ish = set()
    kaash = set()
    s�mbolid = set()
    v�l_s�nastik = {}
    for s�mb in k�ik_s�mb:
        if s�mb in t�ish��likud:
            t�ish.add((s�mb, sagedus[s�mb]))
        elif s�mb in kaash��likud:
            kaash.add((s�mb, sagedus[s�mb]))
        else:
            s�mbolid.add((s�mb, sagedus[s�mb]))
    v�l_s�nastik["T�ish��likud"] = t�ish
    v�l_s�nastik["Kaash��likud"] = kaash
    v�l_s�nastik["Muud"] = s�mbolid
    return v�l_s�nastik