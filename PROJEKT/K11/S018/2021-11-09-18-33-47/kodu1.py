def seosta_lapsed_ja_vanemad(lapsed, nimed):
    with open(lapsed, "r", encoding="UTF-8") as f_l:
        j�r = f_l.read().split("\n")
        vanemlus = {}
        for i in range(len(j�r)):
            j�r[i] = j�r[i].split()
            vanemad = vanemlus.get(j�r[i][1], set())
            vanemad.add(j�r[i][0])
            vanemlus[j�r[i][1]] = vanemad
    with open(nimed, "r", encoding="UTF-8") as f_n:
        j�r = f_n.read().split("\n")
        nimed = {}
        for i in range(len(j�r)):
            j�r[i] = j�r[i].split()
            nimi = ""
            for j in range(len(j�r[i])-1):
                nimi = nimi + j�r[i][j+1] + " "
            nimi = nimi.strip(" ")
            nimed[j�r[i][0]] = nimi
    vanemdatud = {}
    for laps, vanemad in vanemlus.items():
        for ik in vanemad:
            vanem = vanemdatud.get(nimed[laps], set())
            vanem.add(nimed[ik])
            vanemdatud[nimed[laps]] = vanem
    return vanemdatud
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")