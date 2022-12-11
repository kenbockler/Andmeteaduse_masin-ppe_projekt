def loe_failist(fail):
    sõnastik = {}
    f = open(fail, encoding="UTF-8")
    for rida in f:
        elemendid = rida.strip().split(" ")
        sõnastik[elemendid[0]] = " ".join(elemendid[1:])
    f.close()
    return sõnastik
def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
    lapsed_vanemad = {}
    isikukoodid = open(lapsed_fail, encoding="UTF-8")
    nimed = loe_failist(nimed_fail)
    for rida in isikukoodid:
        elemendid = rida.strip().split(" ")
        laps = nimed[elemendid[1]]
        vanemad = set()
        if laps in lapsed_vanemad:
            vanem = lapsed_vanemad[laps]
            vanem.add(nimed[elemendid[0]])
            lapsed_vanemad[laps] = vanem
        else:
            vanemad.add(nimed[elemendid[0]])
            lapsed_vanemad[laps] = vanemad
    isikukoodid.close()
    return lapsed_vanemad
lapsed_vanemad = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for i in lapsed_vanemad:
    vanem = ", ".join(e for e in lapsed_vanemad[i])
    print("{0}: {1}".format(i, vanem))
