import os
hinnad=open("taksohinnad.txt", encoding="utf-8")
if os.stat("taksohinnad.txt").st_size == 0:
    tee_km=float(input("Sisesta tee pikkus kilomeetrites: "))
    print("Fail on tuhi")
else:
    tee_km={}
    while True:
        try:
            tee_km=float(input("Sisesta tee pikkus kilomeetrites: "))
        except ValueError:
            print("Sisesta number")
        else:
            break
    taksod=[]
    for read in hinnad:
        taksod.append(read)
    autod=[]
    sõiduhinnad=[]
    for odavaim in taksod:
        if tee_km=="":
            break
        võrdlus=0
        nimi=odavaim[ 0 : odavaim.index(",")]
        stardi_hind=odavaim.split(',')[1].lstrip().split(',')[0]
        km_hind0=odavaim[odavaim.find(",")+1:]
        km_hind=km_hind0[km_hind0.find(",")+1:]
        kogumaksumus=float(stardi_hind)+tee_km*float(km_hind)
        autod.append(nimi)
        sõiduhinnad.append(kogumaksumus)
    print(f"Kõige odavam on {autod[sõiduhinnad.index(min(sõiduhinnad))]}.")
    hinnad.close()
