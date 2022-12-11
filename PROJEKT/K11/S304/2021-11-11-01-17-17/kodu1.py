from itertools import groupby
from operator import itemgetter
def seosta_lapsed_ja_vanemad(vanemad_lapsed,nimi_isikk):
    f1 = open(vanemad_lapsed)
    f2 = open(nimi_isikk)
    koodidjanimed = {}
    for rida in f2:
        nimi_kood = rida.split()
        koodidjanimed[nimi_kood[0]] = nimi_kood[1]+' '+ nimi_kood[2]
    vanemlaps = {}
    for line in f1:
        vanem_laps = line.split()
        if vanem_laps[0] in koodidjanimed:
            laps = koodidjanimed[vanem_laps[1]]
            vanem = koodidjanimed[vanem_laps[0]]
            if laps not in vanemlaps:
                vanemlaps[laps] = set()
                vanemlaps[laps].add(vanem)
            else:
                vanemlaps[laps].add(vanem)
            laps = 0
            vanem = 0
    f1.close()
    f2.close()
    return vanemlaps  
print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))
        