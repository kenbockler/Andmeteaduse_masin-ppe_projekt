def erinevad_sümbolid(a):
    a = set(a)
    return a
def sümbolite_sagedus(b):
    hulk = set(b)
    sõnastik = {}
    for täht in hulk:
        count = b.count(täht)
        sõnastik[täht] = count
    return sõnastik
def grupeeri(c):
    hulk = set(c)
    täishäälikudd = ["a", "e", "i", "o", "u", "õ", "ä", "ö" "ü"]
    kaashäälikudd = ["b", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v"]
    sõnastik = {}
    täishäälikud = set()
    kaashäälikud = set()
    muu = set()
    for täht in hulk:
        if täht in täishäälikudd:
            arv_t = c.count(täht)
            ennik = (täht, arv_t)
            täishäälikud.add(ennik)
        elif täht in kaashäälikudd:
            arv_k = c.count(täht)
            ennik = (täht, arv_k)
            kaashäälikud.add(ennik)
        else:
            arv_m = c.count(täht)
            ennik = (täht, arv_m)
            muu.add(ennik)
    sõnastik["Täishäälikud"] = täishäälikud
    sõnastik["Kaashäälikud"] = kaashäälikud
    sõnastik["Muu"] = muu
    return sõnastik