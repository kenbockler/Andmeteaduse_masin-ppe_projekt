def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    sõnastik = {}
    loendus = 0
    for täht in sõne:
        sõnastik[täht] = sõnastik.get(täht, 0) + 1
    return sõnastik
def grupeeri(sõne):
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    for võti,väärtus in sümbolite_sagedus(sõne).items():
        if võti in 'AaEeIiOoUuÕõÄäÖöÜü':
            sõnastik['Täishäälikud'].add((võti,väärtus))
        elif võti in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy':
            sõnastik['Kaashäälikud'].add((võti,väärtus))
        else:
            sõnastik['Muud'].add((võti,väärtus))
    return sõnastik
print(grupeeri("sõida tasa üle silla"))