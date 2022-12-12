f = open("taksohinnad.txt", encoding="UTF-8")
tee_pikkus = float(input("Sisestage tee pikkus kilomeetrites: "))
hinnad = []
taksod = []
for rida in f:
    andmed = rida.strip().split(",")
    taksod.append(andmed[0])
    hinnad.append(float(andmed[1]) + float(andmed[2]) * tee_pikkus)
f.close()
if len(hinnad) == 0 and len(taksod) == 0:
    print("Fail on tühi!")
else:
    print("Kõige odavam on: " + taksod[hinnad.index(min(hinnad))])