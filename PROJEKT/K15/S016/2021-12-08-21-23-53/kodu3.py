sisend = input("sisesta failinimi: ")
f = open(sisend, "r", encoding = "UTF-8")
s�idu_pikkused = []
s�idu_hinnad = []
for rida in f:
    osad = rida.split(" ")
    hind = osad[2]
    v�ljumisaegh = osad[0][0:2]
    if v�ljumisaegh.startswith("0"):
        v�ljumisaegh = v�ljumisaegh[1]
    else:
        v�ljumisaegh = v�ljumisaegh
    v�ljumisaegmin = osad[0][3:5]
    if v�ljumisaegmin.startswith("0"):
        v�ljumisaegmin = v�ljumisaegmin[1]
    else:
        v�ljumisaegmin = v�ljumisaegmin
    v�ljaminutites = int(v�ljumisaegmin)/60
    saabumisaegh = osad[1][0:2]
    if saabumisaegh.startswith("0"):
        saabumisaegh = saabumisaegh[1]
    else:
        saabumisaegh = saabumisaegh
    saabumisaegmin = osad[1][3:5]
    if saabumisaegmin.startswith("0"):
        saabumisaegmin = saabumisaegmin[1]
    else:
        saabumisaegmin = saabumisaegmin
    sisseminutites = int(saabumisaegmin)/60
    arvutush = int(saabumisaegh) - int(v�ljumisaegh)
    arvutusmin = float(sisseminutites) - float(v�ljaminutites)
    if arvutusmin < 0:
        arvutush -= 1
        arvutusmin = arvutusmin * (-1)   
    aega_kulub = arvutush + arvutusmin   
    s�idu_pikkused.append(aega_kulub)
    s�idu_hinnad.append(float(hind))
l�him = min(s�idu_pikkused)
odavaim = min(s�idu_hinnad)
if aega_kulub == l�him or hind == odavaim:
    print(rida)
print(s�idu_pikkused)
print(s�idu_hinnad)