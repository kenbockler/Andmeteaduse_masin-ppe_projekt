teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
sisu = ""
TaksoHinnad = []
i = 0
hindadejärjekord = -1
stardihinnaNumber = 1
Kilomeetrihinnanumber = 2
hind = 0
f = open("taksohinnad.txt","r",encoding = "UTF-8")
sisu = f.read().replace("\n",",").split(",")
f.close()
if len(sisu)> 1:
    while i < (len(sisu)/3):
        hind = float(sisu[stardihinnaNumber]) + teepikkus*float(sisu[Kilomeetrihinnanumber])
        TaksoHinnad.append(hind)
        stardihinnaNumber +=3
        Kilomeetrihinnanumber +=3
        i += 1
    vaiksemhind = min(TaksoHinnad)
    i = 0
    indeks = 0
    TsükkliteArv = 0
    for i in TaksoHinnad:
        if i == vaiksemhind:
            indeks = TsükkliteArv
        TsükkliteArv += 1
    if indeks > 0:
        indeks = indeks*3
    print("Kõide odavam on "+str(sisu[indeks])+".")
