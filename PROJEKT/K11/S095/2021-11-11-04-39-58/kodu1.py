def seosta_lapsed_ja_vanemad(lapsed, nimed):
    nimed_id={}
    nimed_data=open(nimed)
    for x in nimed_data.readlines():
        x=x.split()
        nimed_id[x[0]]=x[1]+" "+x[2]
    lapsed_data=open(lapsed)
    id_nimeks=open("id_nimeks.txt", "w")
    lapsed_vanemad_id=[]
    for x in lapsed_data.readlines():
        x=x.split()
        lapsed_vanemad_id+=x
    vahetatud=[]
    for y in lapsed_vanemad_id:
        vahetatud.append(nimed_id[y])
    vanemad_id=[]
    lapsed_id=[]
    laps_ja_vanem={}
    for x, y in zip(vahetatud[::2], vahetatud[1::2]):
        if y in laps_ja_vanem.keys():
            laps_ja_vanem[y].add(x)
        else:
            laps_ja_vanem[y]={x}
    return laps_ja_vanem
    lapsed_ja_vanemad={}
    lapsed_data.close()
    nimed_data.close()
    id_nimeks.close()
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")