def erinevad_sümbolid(a):
    return set(a)
def sümbolite_sagedus(a):
    tähed = a
    sõnastik = []
    tähed = list(tähed)
    for el in tähed:
        if el not in sõnastik:
            sõnastik += el
    arvud = [0]*(len(sõnastik))
    for i in range(len(sõnastik)):
        for el in tähed:
            if sõnastik[i] == el:
                arvud[i] += 1
    lõpp_tulemus = {}
    for I in range(len(sõnastik)):
        lõpp_tulemus[sõnastik[I]] = arvud[I]
    return lõpp_tulemus
a = "sõida tasa üle silla"
täis = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
täis_tähed = []
kaas = list('bdfghjklmnprsšzžtv')
kaas_tähed = []
muu = []
fraas = list(a)
for tä in täis:
    if tä in fraas:
        if tä not in täis_tähed:
            täis_tähed += tä
for k in kaas:
    if k in fraas:
        if k not in kaas_tähed:
            kaas_tähed += k
for el in fraas:
    if el not in täis:
        if el not in kaas:
            if el not in muu:
                muu += el
täis_0 = [0]*len(täis_tähed)
for i in range(len(täis_tähed)):
    for el in fraas:
        if täis_tähed[i] == el:
            täis_0[i] += 1
kaas_0 = [0]*len(kaas_tähed)
for ik in range(len(kaas_tähed)):
    for elk in fraas:
        if kaas_tähed[ik] == elk:
            kaas_0[ik] += 1
a_kaas_0 = kaas_0
a_täis_0 = täis_0 
klõpp_tulemus = {}
for I in range(len(a_kaas_0)):
    klõpp_tulemus[kaas_tähed[I]] = a_kaas_0[I]
tlõpp_tulemus = {}
for I in range(len(a_täis_0)):
    tlõpp_tulemus[täis_tähed[I]] = a_täis_0[I]
print('Täishäälikud : ', tlõpp_tulemus, 'Kaashäälikud : ', klõpp_tulemus)
