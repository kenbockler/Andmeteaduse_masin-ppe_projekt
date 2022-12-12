def seosta_lapsed_ja_vanemad(x, y):
    f_lapsed = open(x, encoding="UTF-8")
    f_nimed = open(y, encoding="UTF-8")
    nimede_sõnastik = {}
    laste_sõnastik = {}
    for rida1 in f_nimed:
        järj1 = rida1.strip().split()
        nimede_sõnastik[järj1[0]] = (" ".join(järj1[1:]))
    for rida2 in f_lapsed:
        järj2 = rida2.strip().split()
        vanemad = set()
        vanem = nimede_sõnastik[järj2[0]]
        laps = nimede_sõnastik[järj2[1]]
        if laps in laste_sõnastik:
            vahehulk = laste_sõnastik[laps]
            vahehulk.add(vanem)
            laste_sõnastik[laps] = vahehulk
        else:
            vanemad.add(vanem)
            laste_sõnastik[laps] = vanemad
    return laste_sõnastik
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")