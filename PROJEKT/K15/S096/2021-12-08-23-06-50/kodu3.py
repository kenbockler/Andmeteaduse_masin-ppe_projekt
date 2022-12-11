import datetime
f = open(input("Sisesta sõiduplaan: "), encoding="UTF-8")
bussiajad = {}
i = 0
hinnad = []
ajad = []
for rida in f:
    v, s, hind = rida.strip().split(" ")
    aeg = datetime.datetime.strptime(s, "%H:%M")-datetime.datetime.strptime(v, "%H:%M")
    ajad.append(aeg)
    hinnad.append(int(hind))
    i += 1
    bussiajad[i] = v, s, int(hind), aeg
f.close()
min_hind = min(hinnad)
min_aeg = min(ajad)
for i in bussiajad:
    if min_aeg in bussiajad[i] or min_hind in bussiajad[i]:
        v, s, h, a = bussiajad[i]
        print(v, s, h)