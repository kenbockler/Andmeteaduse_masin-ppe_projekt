def erinevad_s�mbolid(lause):
    return set(lause)
def s�mbolite_sagedus(lause):
    d ={}
    for t�ht in lause:
        if t�ht in d:
            d[t�ht.lower()] = d[t�ht] + 1
        else:
            d[t�ht.lower()] = 1
    return(d)
def grupeeri(lause):
    s�nastik = s�mbolite_sagedus(lause)
    d ={}
    th = set()
    kh = set()
    otha = set()
    t�ish��likud = ["a","e","i","o","u","�","�","�","�"]
    kaash��likud = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y"]
    for t�ht in s�nastik.keys():
        ennik = (t�ht, s�nastik[t�ht])
        if t�ht in t�ish��likud:
            th.add(ennik)
        elif t�ht in kaash��likud:
            kh.add(ennik)
        else:
            otha.add(ennik)
    d["T�ish��likud"] = th
    d["Kaash��likud"] = kh
    d["Muud"] = otha
    return(d)
print(grupeeri("Hei meeees"))
            