def erinevad_s�mbolid(s�ne):
    a = set(s�ne)
    return a
def s�mbolite_sagedus(s�ne):
    s�nastik = {}
    for el in s�ne:
        if el in s�nastik:
            s�nastik[el] = s�nastik[el] + 1
        else:
            s�nastik[el] = 1
    return s�nastik
def grupeeri(s�ne):
    s�nastik = {}
    s�nastik["T�ish��likud"] = set()
    s�nastik["Kaash��likud"] = set()
    s�nastik["Muud"] = set()
    t�ish��lik = "aeiou����"
    t�ish��likud = set(t�ish��lik)
    kaash��lik = "kptgbdfhszjlmnrv�zywcqx"
    kaash��likud = set(kaash��lik)
    y = s�mbolite_sagedus(s�ne)
    for t�ht in y:
        if t�ht.lower() in t�ish��likud:
            s�nastik["T�ish��likud"].add((t�ht,y[t�ht]))
        elif t�ht.lower() in kaash��likud:
            s�nastik["Kaash��likud"].add((t�ht, y[t�ht]))
        else:
            s�nastik["Muud"].add((t�ht, y[t�ht]))
    return s�nastik
print(grupeeri("s�ida tasa �le silla"))