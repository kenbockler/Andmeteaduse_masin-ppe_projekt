teepikkus = float(input("Sisestage tee pikkus koju kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")
for rida in f:
    t = rida.split()
    stardihind = float(t[1])
    km_hind = float(t[2])
    hind = stardihind + km_hind * teepikkus
    hind.append()
print(hind)
f.close()