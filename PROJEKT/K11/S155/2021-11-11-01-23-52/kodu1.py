fail1 = open("lapsed.txt")
fail2 = open("nimed.txt")
def seosta_lapsed_ja_vanemad(fail1,fail2):
    lapsed = {}
    nimed = {}
    vanemad = {}
    for rida in fail1:
        a = rida.strip().split()
        if a[1] not in lapsed:
            lapsed[a[1]] = a[0]
        else:
            lapsed[a[1]]= {lapsed[a[1]], a[0]}
    for x in fail2:
        rida2 = x.strip().split(' ', 1)
        isikukood = rida2[0]
        nimi = rida2[1]
        if isikukood in lapsed.keys():
            lapsed[nimi] = lapsed.pop(isikukood)
    return lapsed
print(seosta_lapsed_ja_vanemad(fail1,fail2))
fail1.close()
fail2.close()