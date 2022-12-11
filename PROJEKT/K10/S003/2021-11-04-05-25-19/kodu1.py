def erinevad_s�mbolid(s�ne):
    return set(s�ne)
def s�mbolite_sagedus(s�ne):
    s�nastik = {}
    for t�hem�rk in s�ne:
        if t�hem�rk in s�nastik :
            s�nastik[t�hem�rk] = s�nastik[t�hem�rk] + 1
        else :
            s�nastik[t�hem�rk] = 1
    return s�nastik
def grupeeri(s�ne) :
    s�nastik = {}
    s�nastik["T�ish��likud"] = set()
    s�nastik["Kaash��likud"] = set()
    s�nastik["Muud"] = set()
    sagedus = s�mbolite_sagedus(s�ne)
    for key in sagedus:
        if key.lower() in "aeiou����" :
            s�nastik["T�ish��likud"].add((key,sagedus[key]))
        elif key.lower() in "qxcwbydfghjklmnprsztv��" :
            s�nastik["Kaash��likud"].add((key,sagedus[key]))
        else:
            s�nastik["Muud"].add((key,sagedus[key]))
    return s�nastik
            