def erinevad_sümbolid(sõna):
    sõna = set(sõna)
    return sõna
def sümbolite_sagedus(sõna):
    sõnastik = []
    sõna = list(sõna)
    for täht in range(len(sõna)):            
        if täht in sõna:
            tähe_arv = sõna.count(täht)
        else:
            sõnastik += täht
    uus_sõnastik = (täht, tähe_arv)
    return uus_sõnastik
def grupeeri(sõna):
    ss = sümbolite_sagedus(sõna)
sõna = "abccd"
print(sümbolite_sagedus(sõna))
