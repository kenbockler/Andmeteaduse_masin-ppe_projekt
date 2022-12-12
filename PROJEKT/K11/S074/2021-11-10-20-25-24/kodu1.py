def seosta_lapsed_ja_vanemad(lapsed,nimed):
    laps = open("lapsed.txt", "r", encoding = "UTF-8")
    nimi = open("nimed.txt" , "r", encoding = "UTF-8")
    paarid = {}
    lapsed = set()
    nimed = {}
    for rida in laps:
        ik = rida.strip().split(" ")
        lapsed.add((ik[0],ik[1]))
    for rida in nimi:
        ikn = rida.strip().split(" ")
        nimed[ikn[0]] = ikn[1] + " " + ikn[2]
    laps.close
    nimi.close
    for kood, nimi in nimed.items():
        vanemad = set()
        for vanemIK, lapsIK in lapsed:
            if kood ==lapsIK:
                vanemad.add(nimed[vanemIK])
        if len(vanemad) > 0:
            paarid[nimi] = vanemad
    return paarid    