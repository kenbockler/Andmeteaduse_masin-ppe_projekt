def erinevad_sümbolid(tekst):
    x = set(tekst)
    return x
def sümbolite_sagedus(tekst):
    sümbolid = {}
    for täht in tekst:
        sümbolid[täht] = sümbolid.get(täht, 0) + 1
    return sümbolid
def grupeeri(tekst):
    täishäälikud = ["a","e","i","o","u","õ","ä","ö","ü"]
    kaashäälikud = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","š","z","t","v","w","x","y","z"]
    grupeering = {"Täishäälikud":{}, "Kaashäälikud":{}, "Muud":{}}
    sagedused = sümbolite_sagedus(tekst)
    grupp_täishäälik = set()
    grupp_kaashäälik = set()
    grupp_muud = set()
    for täht in tekst:
        if täht.lower() in täishäälikud:
            grupp_täishäälik.add((täht, sagedused[täht]))
        elif täht.lower() in kaashäälikud:
            grupp_kaashäälik.add((täht, sagedused[täht]))
        else:
            grupp_muud.add((täht, sagedused[täht]))
    grupeering["Täishäälikud"] = grupp_täishäälik
    grupeering["Kaashäälikud"] = grupp_kaashäälik
    grupeering["Muud"] = grupp_muud
    return grupeering
