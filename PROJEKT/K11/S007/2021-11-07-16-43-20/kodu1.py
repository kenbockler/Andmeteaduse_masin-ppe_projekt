def seosta_lapsed_ja_vanemad(fail1, fail2):
    fail1 = open("lapsed.txt", encoding = "UTF-8")
    fail2 = open("nimed.txt", encoding="UTF-8")
    laps_ja_vanemad= {}
    nimed = {}
    isikukoodid = []
    for rida in fail1:
        vanemlaps = rida.strip().split(" ",1)
        isikukoodid.append(vanemlaps)
    for rida in fail2:
        inimene_kood = rida.strip().split(" ",1)
        nimed[inimene_kood[0]]= inimene_kood[1]
    for i in range(len(isikukoodid)):
        laps = nimed[isikukoodid[i][1]]
        vanem = nimed[isikukoodid[i][0]]
        if laps in laps_ja_vanemad:
            laps_ja_vanemad[laps].add(vanem)
        else:
            laps_ja_vanemad[laps]= set()
            laps_ja_vanemad[laps].add(vanem)
    return laps_ja_vanemad
s�nastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for v�ti in s�nastik:
    if len(s�nastik[v�ti]) ==2:
        print(v�ti+":",end = " ")
        for vanem in s�nastik[v�ti]:
            print(vanem, end = " ")
        print()
    else:
        print(v�ti+":", end = " ")
        for vanem in s�nastik[v�ti]:
            print(vanem)
