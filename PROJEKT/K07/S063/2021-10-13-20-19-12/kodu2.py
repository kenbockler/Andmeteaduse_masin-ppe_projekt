tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "utf-8")
hinnad = []
for rida in f:
    rida = rida.strip().split(",")
    takso_nimi = rida[0]
    sisse_hind = float(rida[1])
    km_hind = float(rida[2])
    hinnad += [[takso_nimi, sisse_hind + km_hind * tee_pikkus]]
f.close()
try:
    odavam_hind = hinnad[0][1]
    odavam_takso = hinnad[0][0]
    for i in range(len(hinnad)):
        if float(hinnad[i][1]) < odavam_hind:
            odavam_hind = float(hinnad[i][1])
            odavam_takso = hinnad[i][0]
    print("Kõige odavam on", odavam_takso+".")
except:
    print("Kõige odavamat taksot ei saa väljastada.")