f = open("taksohinnad.txt", encoding = "UTF-8")
valikud = []
km = float(input("Sisesta km: "))
if km == "0":
    while True:
        rida = f.readline()
        if rida == "":
            break
        ridasplit = rida.split(",")
        takso_nimi = ridasplit[0]
        taksofirmade_nimekiri.append(takso_nimi)
        sisseistumisehind = float(ridasplit[1])
        km_hind = float(ridasplit[2])
        hind = sisseistumisehind
        valikud.append(hind)
else:
    taksofirmade_nimekiri = []
    while True:
        rida = f.readline()
        if rida == "":
            break
        ridasplit = rida.split(",")
        takso_nimi = ridasplit[0]
        taksofirmade_nimekiri.append(takso_nimi)
        sisseistumisehind = float(ridasplit[1])
        km_hind = float(ridasplit[2])
        hind = sisseistumisehind + km_hind * km
        valikud.append(hind)
try:
    odavaim = min(valikud)
    j�rk = valikud.index(odavaim)
    v�ljund_l�puks = taksofirmade_nimekiri[j�rk]
    print("K�ige odavam on ", v�ljund_l�puks)
except:
    print()
f.close()