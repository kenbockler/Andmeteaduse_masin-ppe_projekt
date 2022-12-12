def erinevad_s�mbolid(s�ne):
    return set(s�ne)
def s�mbolite_sagedus(s�ne):
    s�nastik = {}
    for el in s�ne:
        if el not in s�nastik:
            kogus = int(s�ne.count(el))
            s�nastik[el] = kogus
    return s�nastik
def grupeeri(s�ne):
    vokaalid = "eEUuIioO����aA����"
    konsonandid = "qQwWrRtTyYpPsS��dDfFgGhHjJkKlLzZ��xXcCvVbBnNmM"
    t�ish��likud = set()
    kaash��likud = set()
    muud = set()
    s�nastik = {}
    for el in s�ne:
        if el in vokaalid:
            if el not in t�ish��likud:
                kogus = int(s�ne.count(el))
                t�ish��likud.add((el, kogus))
        elif el in konsonandid:
            if el not in kaash��likud:
                kogus = int(s�ne.count(el))
                kaash��likud.add((el, kogus))
        elif el not in muud:
            kogus = int(s�ne.count(el))
            muud.add((el, kogus))
    s�nastik["T�ish��likud"] = t�ish��likud
    s�nastik["Kaash��likud"] = kaash��likud
    s�nastik["Muud"] = muud
    return s�nastik
