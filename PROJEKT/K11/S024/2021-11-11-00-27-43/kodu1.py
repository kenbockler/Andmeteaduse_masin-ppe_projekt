def seosta_lapsed_ja_vanemad(f1, f2):
    f_lapsed = open(f1, encoding="UTF-8")
    f_nimed = open(f2, encoding="UTF-8")
    s�nastik = {}
    s�nastik1 = {}
    s�nastik2 = {}
    uus_rida1 = []
    uus_rida2 = []
    laste_koodid = []
    for rida1 in f_lapsed:
        rida1 = rida1.split(" ",2)
        rida1[-1] = rida1[-1].strip()
        uus_rida1.append(rida1)
        laste_koodid.append(rida1[1])
        for i in range(len(uus_rida1)):
            s�nastik1[uus_rida1[i][0]] = uus_rida1[i][1]
    for rida2 in f_nimed:
        rida2 = rida2.strip("\n").split(" ",1)
        uus_rida2.append(rida2)
    for i in range(len(uus_rida2)):
        s�nastik2[uus_rida2[i][0]] = uus_rida2[i][1]
    for k in range(len(laste_koodid)):
        vanema_kood = list(s�nastik1.keys())[list(s�nastik1.values()).index(laste_koodid[k])]
        vanema_nimi = s�nastik2[vanema_kood]
        lapse_nimi = s�nastik2[laste_koodid[k]]
        if lapse_nimi not in s�nastik:
            s�nastik[lapse_nimi] = set()
            s�nastik[lapse_nimi].add(vanema_nimi)
        else:
            s�nastik[lapse_nimi].add(vanema_nimi)
    f_lapsed.close()
    f_nimed.close()
    print(s�nastik)
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))