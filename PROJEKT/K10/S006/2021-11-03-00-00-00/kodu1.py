def erinevad_s�mbolid(lause):
    return set(lause)
def s�mbolite_sagedus(lause):
    s�nastik = {}
    s�mbolid = list(lause)
    for s�mbol in s�mbolid:
        if s�mbol in s�nastik:
            s�nastik[s�mbol] = s�nastik[s�mbol] + 1
        else:
            s�nastik[s�mbol] = 1
    return s�nastik
def grupeeri(lause):
    t�ish��likud = list("aeiou����AEIOU����")
    kaash��likud = list("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM")
    s�nastik = {}
    s�nastik["T�ish��likud"] = set()
    s�nastik["Kaash��likud"] = set()
    s�nastik["Muud"] = set()
    for s�mbol in lause:
        if s�mbol in t�ish��likud:
            s�nastik["T�ish��likud"].add((s�mbol, lause.count(s�mbol)))
        elif s�mbol in kaash��likud:
            s�nastik["Kaash��likud"].add((s�mbol, lause.count(s�mbol)))
        else:
            s�nastik["Muud"].add((s�mbol, lause.count(s�mbol)))
    return(s�nastik)