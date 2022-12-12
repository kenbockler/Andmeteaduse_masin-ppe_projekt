'''-- Kodutöö nr. 11 - 1. Lapsed ja vanemad --'''
'''Kirjuta programm, mis väljastab ekraanile iga lapse kohta ühe rea: nimi, koolon, tühik ning
   seejärel koma ja tühikuga eraldatuna ema ja isa nimi. Kui teada on ainult üks vanem, siis
   väljastada ainult see.'''
def lapse_vanemad(laste_fail):
    f = open(laste_fail)
    lapsed = {}
    for rida in f:
        andmed = rida.strip().split()
        lapse_id = andmed[1]
        vanema_id = andmed[0]
        if lapse_id not in lapsed:
            lapsed[lapse_id] = set()
        lapsed[lapse_id].add(vanema_id)    
    f.close()
    return lapsed
def id_nimed(nimede_fail):
    f = open(nimede_fail, encoding = 'utf-8')
    nimed = {}
    for rida in f:
        andmed = rida.strip().split()
        nimed[andmed[0]] = ' '.join(andmed[1:])
    f.close()
    return nimed
def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    lapsed = lapse_vanemad(laste_fail)
    nimed = id_nimed(nimede_fail)
    lapsed_vanemad = {}
    for lapse_id in lapsed:
        vanemad = set()
        for vanema_id in lapsed[lapse_id]:
            vanemad.add(nimed[vanema_id])
        lapsed_vanemad[nimed[lapse_id]] = vanemad
    return lapsed_vanemad
lapsed_vanemad = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for laps in lapsed_vanemad:
    print(laps, end = ': ')
    print(', '.join(lapsed_vanemad[laps]))