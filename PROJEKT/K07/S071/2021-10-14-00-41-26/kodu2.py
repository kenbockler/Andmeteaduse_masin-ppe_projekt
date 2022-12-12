import sys
tee_pikkus = float(input("Tee pikkus km: "))
def hind(sisse,km_hind,mitu_km):
    km_hind = float(km_hind)
    summa = float(sisse)
    summa += km_hind * mitu_km
    return round(summa,2)
fail = open("taksohinnad.txt", encoding="UTF-8")
fail.seek(0)
esimene = fail.read(1)
if not esimene:
    sys.exit('"taksohinnad.txt" on tühi')
else:
    fail.seek(0)
nimekiri = []
for rida in fail.readlines():
    rida = rida.rstrip("\n")
    nimekiri += rida.split(",")
fail.close()
odavaim = []
x = 1
y = 2
i = 0
while i < len(nimekiri):
    odavaim.append(hind(nimekiri[x],nimekiri[y],tee_pikkus))
    i += 3
    x += 3
    y += 3
kõige_odavam_hind = min(odavaim)
milline_takso = odavaim.index(kõige_odavam_hind)
if milline_takso == 0:
    vastus = nimekiri[0]
else:
    vastus = nimekiri[milline_takso * 3]
print("Kõige odavam on", vastus + ".")