km_input = float(input("Sisesta tee pikkus kilomeetrites: "))
try:
    f = open("taksohinnad.txt", "r")
    taksod = []
    hinnad = []
    while True:
        rida = f.readline()
        if rida == "":
            break
        else:
            rida1 = rida.strip().split(",")
            takso = rida1[0]
            sisse = float(rida1[1])
            km_hind = float(rida1[2])
            hind_kokku = sisse + (km_hind * km_input)
            taksod.append(takso)
            hinnad.append(hind_kokku)
    print(taksod[hinnad.index(min(hinnad))])
except:
    print("Taksod puuduvad")
f.close()
