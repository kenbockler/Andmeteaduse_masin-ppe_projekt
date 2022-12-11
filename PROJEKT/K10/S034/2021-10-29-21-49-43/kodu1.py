def erinevad_sümbolid(sõne):
    hulk = set(list(sõne))
    return(hulk)
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for element in sõne:
        if element in sõnastik:
            sõnastik[element] = sõnastik[element] + 1
        else:
            sõnastik[element] = 1
    return(sõnastik)
def grupeeri(sõne):
    Täishäälikud = list('AEIOUÖÄÜÕaeiouöäüõa')
    Kaashäälikud = list('BCDFGHJKLMNPQRSŠZŽTVWXYbcdfghjklmnpqrsšzžtvwxy')
    Muud = (list('!"
    täishäälikud = {}
    kaashäälikud = {}
    muud = {}
    for element in sõne:
        if element in Täishäälikud:
            if element in täishäälikud:
                täishäälikud[element] = täishäälikud[element] + 1
            else:
                täishäälikud[element] = 1
        elif element in Kaashäälikud:
            if element in kaashäälikud:
                kaashäälikud[element] = kaashäälikud[element] + 1
            else:
                kaashäälikud[element] = 1
        else:
            if element in muud:
                muud[element] = muud[element] + 1
            else:
                muud[element] = 1
    hulga_paarid_t = set()
    for võti, väärtus in täishäälikud.items():
        hulga_paarid_t.add((võti ,väärtus))
    hulga_paarid_k = set()
    for võti, väärtus in kaashäälikud.items():
        hulga_paarid_k.add((võti ,väärtus))
    hulga_paarid_m = set()
    for võti, väärtus in muud.items():
        hulga_paarid_m.add((võti ,väärtus))
    sõnastik = {}
    sõnastik['Täishäälikud'] = hulga_paarid_t
    sõnastik['Kaashäälikud'] = hulga_paarid_k
    sõnastik['Muud'] = hulga_paarid_m
    return sõnastik