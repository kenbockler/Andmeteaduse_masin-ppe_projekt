import string
def erinevad_s�mbolid(s�ne):
    hulk = set()
    for s�mbol in s�ne:
        hulk.add(s�mbol)
    return hulk
def s�mbolite_sagedus(s�ne1):
    s�nastik1 = {}
    for t�ht in s�ne1:
        if t�ht in s�nastik1:
            s�nastik1[t�ht] = s�nastik1[t�ht] + 1
        else:
            s�nastik1[t�ht] = 1
    return s�nastik1
def grupeeri(s�ne):
    s�nastik1 = s�mbolite_sagedus(s�ne)
    s�nastik2 = {}
    s�nastik2["T�ish��likud"] = set()
    s�nastik2["Kaash��likud"] = set()
    s�nastik2["Muud"] = set()
    t�ish��likud = ["a", "e", "i", "o", "u", "�", "�", "�", "�"]
    kaash��likud = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "�", "z", "�", "t", "v", "w", "y", "x"] 
    muud = list(string.punctuation) + [" "]
    for t�ht in s�ne:
        v�iket�ht = t�ht.lower()
        if v�iket�ht in t�ish��likud:
            s�nastik2["T�ish��likud"].add((t�ht, s�nastik1[t�ht]))
        elif v�iket�ht in kaash��likud:
            s�nastik2["Kaash��likud"].add((t�ht, s�nastik1[t�ht]))
        elif v�iket�ht in muud:
            s�nastik2["Muud"].add((t�ht, s�nastik1[t�ht]))
    return s�nastik2