a='aias sadas saia, nõnda arvas Kaia, tulles väravast läbi, mööda teed laia'
def erinevad_sümbolid(sõne):
    sõne_hulk = set(sõne)
    return sõne_hulk
print(erinevad_sümbolid(a))
sõnastik ={}
def sümbolite_sagedus(sõne):
    for el in list(sõne):
        sõnastik[el] = sõnastik.get(el, 0) + 1
    return sõnastik
print(sümbolite_sagedus(a))
vokaalid = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü']
konsonandid = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'z', 't', 'v', 'B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'Z', 'T', 'V']
märgid = ['.', ',', ' ', '!', '?', ';', ':']
sõne_järjend_v =[]
sõne_järjend_k =[]
sõne_järjend_m =[]
sõnastik_v = {}
sõnastik_k ={}
sõnastik_m = {}
def grupeeri(sõne):
    sõne_järjend = list(sõne)
    for el in sõne_järjend:
        if el in vokaalid:
            sõne_järjend_v.append(el)
            for el_v in sõne_järjend_v:
                sõnastik_v[el_v] = sõnastik_v.get(el_v, 0) + 1
        if el in konsonandid:
            sõne_järjend_k.append(el)
            for el_k in sõne_järjend_k:
                sõnastik_k[el_k] = sõnastik_k.get(el_k, 0) + 1
        if el in märgid:
            sõne_järjend_m.append(el)
            for el_m in sõne_järjend_m:
                sõnastik_m[el_m] = sõnastik_m.get(el_m, 0) + 1
    return ("Vokaalid: ",  sõnastik_v, "Konsonandid: ",  sõnastik_k, "Märgid: ",  sõnastik_m)
print(grupeeri(a))