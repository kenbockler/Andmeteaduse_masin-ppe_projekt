def seosta_lapsed_ja_vanemad(x, y):
    f_lapsed = open(x, encoding="UTF-8")
    f_nimed = open(y, encoding="UTF-8")
    nimede_s�nastik = {}
    laste_s�nastik = {}
    for rida1 in f_nimed:
        j�rj1 = rida1.strip().split()
        nimede_s�nastik[j�rj1[0]] = (" ".join(j�rj1[1:]))
    for rida2 in f_lapsed:
        j�rj2 = rida2.strip().split()
        vanemad = set()
        vanem = nimede_s�nastik[j�rj2[0]]
        laps = nimede_s�nastik[j�rj2[1]]
        if laps in laste_s�nastik:
            vahehulk = laste_s�nastik[laps]
            vahehulk.add(vanem)
            laste_s�nastik[laps] = vahehulk
        else:
            vanemad.add(vanem)
            laste_s�nastik[laps] = vanemad
    return laste_s�nastik
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")