def seosta_lapsed_ja_vanemad(lapsedfail, nimedfail):
    lapsed = open(lapsedfail)
    nimed = open(nimedfail)
    isik_nimi = {}
    isikud2 = {}
    seostatudlapjavan = {}
    for rida in nimed:
        nimi_isik = rida.split()
        nimi = nimi_isik[1] + " " + nimi_isik[2]
        isik_nimi[nimi_isik[0]] = nimi
    for rida in lapsed:
        isikud = rida.split()
        isikudvan = isikud[0]
        isikudlap = isikud[1]
        if isikudlap in isikud2.keys():
            isikud2[isikudlap] = (isikud2[isikudlap],isikudvan)
        else:
            isikud2[isikudlap] = isikudvan            
    for l,v in isikud2.items():
        laps_nimi = isik_nimi[l]
        vanemate_nimid = set()
        if len(v) == 11:
            x = isik_nimi[v]
            vanemate_nimid.add(x)
        else:
            van1,van2 = v
            vanemate_nimid.add(isik_nimi[van1])
            vanemate_nimid.add(isik_nimi[van2])
        seostatudlapjavan[laps_nimi] = vanemate_nimid
    return seostatudlapjavan
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
            