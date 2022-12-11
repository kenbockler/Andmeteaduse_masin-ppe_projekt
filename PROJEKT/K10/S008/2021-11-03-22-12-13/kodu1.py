def erinevad_sümbolid(lause):
    return set(lause)
def sümbolite_sagedus(lause):
    d ={}
    for täht in lause:
        if täht in d:
            d[täht.lower()] = d[täht] + 1
        else:
            d[täht.lower()] = 1
    return(d)
def grupeeri(lause):
    sõnastik = sümbolite_sagedus(lause)
    d ={}
    th = set()
    kh = set()
    otha = set()
    täishäälikud = ["a","e","i","o","u","ü","ö","õ","ä"]
    kaashäälikud = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y"]
    for täht in sõnastik.keys():
        ennik = (täht, sõnastik[täht])
        if täht in täishäälikud:
            th.add(ennik)
        elif täht in kaashäälikud:
            kh.add(ennik)
        else:
            otha.add(ennik)
    d["Täishäälikud"] = th
    d["Kaashäälikud"] = kh
    d["Muud"] = otha
    return(d)
print(grupeeri("Hei meeees"))
            