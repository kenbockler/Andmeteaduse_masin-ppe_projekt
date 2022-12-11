def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne2):
    sõnastik = {}
    for el in sõne2:
        if el not in sõnastik:
            arv = sõne2.count(el)
            sõnastik[el] = arv
    return sõnastik
täishäälikud = 'AEIOUÕÄÖÜaeiouõäöü'
kaashäälikud = 'BCDFGHJKLMNPQRSŠZŽTVWXYbcdfghjklmnpqrsšzžtvwxy'
def grupeeri(sõne3):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    for el in sõne3:
        if el in täishäälikud:
           arv = sõne3.count(el)
           sõnastik["Täishäälikud"].add((el, arv))
        elif el in kaashäälikud:
           arv = sõne3.count(el)
           sõnastik["Kaashäälikud"].add((el, arv)) 
        else:
            arv = sõne3.count(el)
            sõnastik["Muud"].add((el, arv))
    return sõnastik
        