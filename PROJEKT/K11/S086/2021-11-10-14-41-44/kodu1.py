def seosta_lapsed_ja_vanemad(fail_idlaps_idvanem, fail_id_isik):
    koodid = {}
    väljund = {}
    f = open(fail_id_isik)
    for rida in f.readlines():
        rida = rida.strip().split(" ",1)
        koodid[rida[0]] = rida[1]
    f.close()
    f = open(fail_idlaps_idvanem)
    for rida in f.readlines():
        rida = rida.strip().split()
        rida[0] = koodid[rida[0]]
        rida[1] = koodid[rida[1]]
        väljund.setdefault(rida[1], set())
        väljund[rida[1]].add(rida[0])
    f.close()
    return väljund
    