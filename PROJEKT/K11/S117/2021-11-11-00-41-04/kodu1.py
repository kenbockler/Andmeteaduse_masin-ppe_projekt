def seosta_lapsed_ja_vanemad(lapsed_f, nimed_f):
    f1 = open(lapsed_f)
    f2 = open(nimed_f)
    sonastik = {}
    lisa_sonastik1 = {}
    lisa_sonastik2 = {}
    for rida in f1:
        rida = rida.strip()
        rida1 = rida.split(' ')
        if rida1[1] in lisa_sonastik2.keys():
            lisa_sonastik2[rida1[1]] = [lisa_sonastik2[rida1[1]], rida1[0]]
        else:
            lisa_sonastik2[rida1[1]] = rida1[0]
    for rida in f2:
        rida = rida.strip()
        rida2 = rida.split(' ')
        lisa_sonastik1[rida2[0]] = rida2[1] + ' ' + rida2[2]
    for i in lisa_sonastik2.keys():
        sonastik[lisa_sonastik1[i]] = set()
        vanema_id = lisa_sonastik2[i]
        if type(vanema_id) == str:
            sonastik[lisa_sonastik1[i]].add(lisa_sonastik1[vanema_id])
        else:
            sonastik[lisa_sonastik1[i]].add(lisa_sonastik1[vanema_id[0]])
            sonastik[lisa_sonastik1[i]].add(lisa_sonastik1[vanema_id[1]])
    f1.close()
    f2.close()
    return sonastik