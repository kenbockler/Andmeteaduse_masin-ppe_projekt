def seosta_lapsed_ja_vanemad(lapsed_txt, nimed_txt):
    lapsed = dict()
    with open("lapsed.txt") as fail:
        for rida in fail:
            veerud = rida.strip().split()
            lapsed.setdefault(veerud[1], [])
            lapsed[veerud[1]].append(veerud[0])
    nimed = dict()
    with open("nimed.txt") as fail:
        for rida in fail:
            veerud = rida.strip().split()
            nimed[veerud[0]] = veerud[1] + " " + veerud[2]
    vastus = dict()
    for m in lapsed:
        vanemad = set()
        for e in lapsed[m]:
            vanemad.add(nimed[e])
        vastus.setdefault(nimed[m], [])
        vastus[nimed[m]] = vanemad
    return vastus
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))