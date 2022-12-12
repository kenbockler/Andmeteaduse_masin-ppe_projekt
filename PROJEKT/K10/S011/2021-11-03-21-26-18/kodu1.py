def erinevad_s�mbolid(s�ne):
    s�mbolite_hulk = set(s�ne)
    return (s�mbolite_hulk)
def s�mbolite_sagedus(s�ne):
    s�nastik = {}
    for s�mbol in s�ne:
        s�nastik[s�mbol] = s�nastik.get(s�mbol, 0) + 1
    return (s�nastik)
def grupeeri(s�ne):
    s�nastik = {}
    t�ish = {}
    sulgh = {}
    muu = {}
    t�ish��likud = ("a", "e", "i", "o", "u", "�", "�", "�", "�")
    kaash��likud = ("k", "p", "t", "g", "b", "d", "s", "c", "f", "h", "j", "l", \
                    "m", "n", "q", "r", "v", "w", "x", "y", "z", "�", "�")
    for s�mbol in s�ne:
        if s�mbol in t�ish��likud:
            t�ish[s�mbol] = t�ish.get(s�mbol, 0) + 1
            s�nastik["T�ish��likud"] = t�ish
        elif s�mbol in kaash��likud:
            sulgh[s�mbol] = sulgh.get(s�mbol, 0) + 1
            s�nastik["Kaash��likud"] = sulgh
        else:
            muu[s�mbol] = muu.get(s�mbol, 0) + 1
            s�nastik["Muud"] = muu
    return (s�nastik)