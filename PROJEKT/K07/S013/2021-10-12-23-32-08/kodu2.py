f=open("taksohinnad.txt", encoding="UTF-8")
x =float(input("Sisesta tee pikkus kilomeetrites: "))
nimed = []
j�rjend = []
for rida in f:
    j�rjend1 = rida.strip()
    j�rjend1 = j�rjend1.split(",")
    nimi = j�rjend1[0]
    nimed.append(nimi)
    start = float(j�rjend1[1])
    tasu = float(j�rjend1[2])
    hind = str(start + (x * tasu))
    j�rjend.append(float(hind))
indeks = 0
miinimum = j�rjend[0]
for i in range(len(j�rjend)):
    if j�rjend[i] < miinimum:
        miinimum = j�rjend[i]
        indeks = i
print("K�ige odavam on " + str((nimed[indeks])))
f.close()