def erinevad_s�mbolid(s�ne):
    hulk = set(s�ne)
    return hulk
def s�mbolite_sagedus(s�ne):
    d = {}
    j�rjend = list(s�ne)
    for el in j�rjend:
        if el in d:
            d[el] = d[el] + 1
        else:
            d[el] = 1
    return d
def grupeeri(s�ne):
    d = {}
    t�ish��likud = ("a", "e", "i", "o", "u", "�", "�", "�", "�")
    kaash��likud = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "�", "z", "�", "t", "v", "w", "x", "y")
    j�rjend = list(s�ne)
    t�is = set()
    kaas = set()
    muud = set()
    for el in j�rjend:
        d[el] = d.get(el, 0) + 1
    uus_j�rjend = [(k, v) for k, v in d.items()]
    for i in range(len(uus_j�rjend)):
        for j in uus_j�rjend[i][0]:
            if j.lower() in t�ish��likud:
               t�is.add(uus_j�rjend[i])
            elif j.lower() in kaash��likud:
                kaas.add(uus_j�rjend[i])
            else:
                muud.add(uus_j�rjend[i])
    s�nastik = {}
    s�nastik["T�ish��likud"] = t�is
    s�nastik["Kaash��likud"] = kaas
    s�nastik["Muud"] = muud
    return s�nastik
 