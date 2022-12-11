pikkus= float(input("Sisesta tee pikkus kilomeetrites: "))
odavaim_hind = 100000
f = open("taksohinnad.txt")
for rida in f:
    a = rida.split(",")
    sisseistumise_hind= float(a[1])
    km_hind= float(a[2])
    maksumus = sisseistumise_hind+pikkus*km_hind
    if maksumus < odavaim_hind:
        odavaim_hind = maksumus
        odavaim_nimi=a[0]
if pikkus ==0:
    odavaim_nimi="jala minna"
print("Kõige odavam on ", odavaim_nimi.strip(), ".")
f.close()