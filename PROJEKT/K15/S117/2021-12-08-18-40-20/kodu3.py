fail = input('Sisesta failinimi: ')
f = open(fail)
halvad_ajad = set()
sisend = f.readlines()
sisend.sort()
for rida in sisend:
    rida1 = rida.strip().split()
    valjumis = rida1[0]
    saabumis = rida1[1]
    hind = int(rida1[2])
    for teine_rida in sisend:
        rida2 = teine_rida.strip().split()
        valjumis1 = rida2[0]
        saabumis1 = rida2[1]
        hind1 = int(rida2[2])
        if valjumis < valjumis1 and saabumis > saabumis1 and hind > hind1: 
            halvad_ajad.add(rida)
f.close()
for i in sisend:
    if i not in halvad_ajad:
        print(i.strip())