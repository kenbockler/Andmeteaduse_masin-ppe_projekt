fail_1 ="lapsed.txt"
fail_2 = "nimed.txt"
def  seosta_lapsed_ja_vanemad(fail_1, fail_2):
    f = open(fail_1)
    read = f.readlines()
    f.close()
    lapsed_id = []
    vanemad_id = []
    for rida in read:
        isikukoodid = (rida.strip("\n")).split(" ")
        vanemad_id.append(isikukoodid[0])
        lapsed_id.append(isikukoodid[1])
    f = open(fail_2)
    nim_read = f.readlines()
    f.close()
    nimed = []
    nime_id = []
    for rida in nim_read:
        isik_nimi = (rida.strip("\n")).split(" ")
        nimed.append(isik_nimi[1]+" "+isik_nimi[2])
        nime_id.append(isik_nimi[0])
    s�nastik = {}
    for el in lapsed_id:
        lapsevanema_id = vanemad_id[lapsed_id.index(el)]
        lapse_nimi = nimed[nime_id.index(el)]
        lapsevanema_nimi = nimed[nime_id.index(lapsevanema_id)]
        if lapse_nimi not in s�nastik:
            lapsevanemate_nimed = set()
            s�nastik[lapse_nimi]= lapsevanemate_nimed
            s�nastik[lapse_nimi].add(lapsevanema_nimi)
        else:
            s�nastik[lapse_nimi].add(lapsevanema_nimi)
    return s�nastik
printimiseks = seosta_lapsed_ja_vanemad(fail_1, fail_2)
for lapse_nimi, lapsevanemate_nimed in printimiseks.items():
    print(lapse_nimi, ": ", str(lapsevanemate_nimed))
