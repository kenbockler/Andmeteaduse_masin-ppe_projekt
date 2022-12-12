def seosta_lapsed_ja_vanemad(koodid, nimed):
    f_nimed = open(nimed)
    d1 = {}
    for rida in f_nimed:
        andmed = rida.strip().split()
        d1[andmed[0]] = d1.get(andmed[0], (str(andmed[1] + " " + andmed[2])))
    f_nimed.close()
    f_koodid = open(koodid)
    d2 = {}
    for rida in f_koodid:
        andmed = rida.strip().split()
        if andmed[1] in d1.keys():
            laps = d1[andmed[1]]
        if andmed[0] in d1.keys():
            vanem = d1[andmed[0]]
        if laps not in d2:
            d2[laps] = set()
            d2[laps].add(vanem)
        else:
            d2[laps].add(vanem)
    f_koodid.close()
    return d2
