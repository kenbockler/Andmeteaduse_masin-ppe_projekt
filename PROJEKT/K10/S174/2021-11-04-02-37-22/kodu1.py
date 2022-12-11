def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        if täht in sõnastik:
            sõnastik[täht] += 1
        else:
            sõnastik[täht] = 1
    return sõnastik
def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud sümbolid"] = set()
    for täht in sõne:
        if täht in "aeiouõäöü":
            sõnastik["Täishäälikud"].add((täht, sümbolite_sagedus(sõne).get(täht)))
        elif täht in "bdfghjklmnprsšzžtvqwxy":
            sõnastik["Kaashäälikud"].add((täht, sümbolite_sagedus(sõne).get(täht)))
        else:
            sõnastik["Muud sümbolid"].add((täht, sümbolite_sagedus(sõne).get(täht)))
    return sõnastik
    