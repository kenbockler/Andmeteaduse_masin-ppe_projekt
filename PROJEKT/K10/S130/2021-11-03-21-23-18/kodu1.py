def erinevad_sümbolid(sõne):
    leitud = set(sõne)& set(sõne)
    return leitud
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        sõnastik[el] = sõnastik.get(el, 0) + 1
    return sõnastik
def grupeeri(sõne):
    a = {'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü', 'a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü'}
    b = {'x', 'c', 'q', 'y', 'w', 'h', 'j', 'l', 'm', 'n', 'r', 's', 't', 'v', 'k', 'p', 'g', 'b', 'd', 'f', 'š', 'z', 'ž',
        'X', 'C', 'Q', 'Y', 'W', 'H', 'J', 'L', 'M', 'N', 'R', 'S', 'T', 'V', 'K', 'P', 'G', 'B', 'D', 'F', 'Š', 'Z', 'Ž'}
    kui_palju = sümbolite_sagedus(sõne)
    taishaalikud = set()
    kaashaalikud = set()
    muud = set()
    tähed = {}
    for el in sõne:
        if el in a:
            taishaalikud.add((el, kui_palju[el]))
        elif el in b:
            kaashaalikud.add((el, kui_palju[el]))
        else:
            muud.add((el, kui_palju[el]))
        tähed['Täishäälikud'] = taishaalikud
        tähed['Kaashäälikud'] = kaashaalikud
        tähed['Muud'] = muud
    return tähed
        