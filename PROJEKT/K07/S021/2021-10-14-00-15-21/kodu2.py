f = open("taksohinnad.txt", encoding = "UTF-8")
teepikkus = float(input("Sisestage tee pikkus kilomeetrites: "))
seni_odavaim = None
odavaim = ""
for rida in f:
    j�rjend = rida.strip().split(",")
    sisseastumise_hind = j�rjend[1]
    kilomeetri_hind = j�rjend[2]
    hind = teepikkus*float(kilomeetri_hind)+float(sisseastumise_hind)
    if seni_odavaim == None or hind < seni_odavaim:
        seni_odavaim = hind
        odavaim = j�rjend[0]
    else:
        continue
print("K�ige odavam on " + odavaim)
f.close()