from math import pi
def koogi_hind(nimi, m��t):
    if nimi == 'ploomikook' or nimi == 'Ploomikook':
        pindala = pi * m��t ** 2
        return round((pindala * 0.04), 2)
    elif nimi == 'Napoleoni kook' or nimi == 'napoleoni kook':
        pindala = m��t ** 2
        return round((pindala * 0.10), 2)
    elif nimi == '�okolaadikook' or nimi == '�okolaadikook':
        pindala = pi * m��t ** 2
        return round((pindala * 0.06), 2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud')
while True:
    nimi = str(input('Sisestage koogi nimi '))
    if nimi == '':
        break
    m��t = float(input('Sisestage koogi m��t '))
    print(koogi_hind(nimi, m��t))
