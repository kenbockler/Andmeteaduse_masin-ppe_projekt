'''
Kirjuta funktsioon koogi_hind, mis võtab argumentideks koogi nime ning mõõdu
ja tagastab koogi maksumuse eurodes, ümardatult teise komakohani
'''
from math import pi
def koogi_hind (kook, mõõt):
    if kook!= 'šokolaadikook' and kook!= 'ploomikook' and kook!= 'Napoleoni kook':
        raise Exception('Sellist kooki andmebaasist ei leitud')
    if kook== 'šokolaadikook' or kook== 'ploomikook':
        pindala= pi*mõõt**2
        if kook== 'šokolaadikook':
            hind= 0.06
            return round(pindala* hind, 2)
        if kook== 'ploomikook':
            hind= 0.04
            return round(pindala* hind, 2)
    else:
        kook== 'Napoleoni kook'
        pindala= mõõt**2
        hind= 0.1
        return round(pindala* hind, 2)
while True:
    nimi= input('Sisesta koogi nimi:')
    if nimi == '':
        break
    mõõt= float(input('Sisesta koogi mõõt:'))
    print('Sisestatud mõõduga '+ nimi.replace('kook', 'koogi ')\
          +'hind on '+ str(koogi_hind(nimi, mõõt))+'€')
    print('ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ')
    