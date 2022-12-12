kaugus = float(input("Sisesta tee pikkus kilomeetrites: "))
taksode_hinnad = []
nimed = []
km = []
fail = open("taksohinnad.txt", encoding="UTF-8")
for rida in fail:
    eraldi = rida.split(",")
    takso_hind = eraldi[1:2]
    nimi = eraldi[0:1]
    km_hind = eraldi[2:3]
    taksode_hinnad.append(takso_hind)
    nimed.append(nimi)
    km.append(km_hind)
    hind = taksode_hinnad + kaugus * km
    väikseim = min(hind)
    indeks = hind.index(väikseim)
    print(nimed(indeks))
fail.close()