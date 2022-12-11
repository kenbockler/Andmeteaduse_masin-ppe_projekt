def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lapsed = open("lapsed.txt", "r")
    nimed = open("nimed.txt", "r")
    tulemus = {}
    kood = {}
    sõnastik = {}
    laps = set()
    vanemad = set()
    for rida in nimed:
        nimi = rida.strip()
        nimi = rida.split(" ", 1)
        sõnastik[nimi[0].strip()] = nimi[1].strip()
        lapse_nimi = sõnastik[nimi[0].strip()]
    for rida in lapsed:
        isikukood = rida.split(" ")
        vanema_kood = isikukood[0].strip()
        lapse_kood = isikukood[1].strip()
        lapse_nimi = sõnastik[lapse_kood]
        vanema_nimi = sõnastik[vanema_kood]
        vanemad = set()
        if lapse_nimi not in tulemus:
            vanemad.add(vanema_nimi)
            tulemus[lapse_nimi] = vanemad
        else:
            vanemad = tulemus[lapse_nimi]
            vanemad.add(vanema_nimi)
            tulemus[lapse_nimi] = vanemad
    return tulemus
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))