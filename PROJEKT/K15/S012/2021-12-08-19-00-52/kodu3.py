def h_min(sisend):
    kellaaeg = sisend.split(":")
    minutid = int(kellaaeg[0])*60 + int(kellaaeg[1])
    return minutid
fail = input("Sisesta failinimi: ")
print("Esimesest linnast teise s�itmiseks v�iksid kaaluda j�rgmisi busse: ")
f = open(fail)
s�idud = []
hinnad = []
for rida in f:
    j�rjend = rida.split(" ")
    v�ljumisaeg = h_min(j�rjend[0])
    saabumisaeg = h_min(j�rjend[1])
    hind = int(j�rjend[2])
    hinnad.append(hind)
    s�idu_kestvus = saabumisaeg - v�ljumisaeg
    s�idud.append(s�idu_kestvus)
l�him_kestvus = min(s�idud)
madalaim_hind = min(hinnad)
f.close()
f = open(fail)
j�rjekord = []
for rida in f:
    j�rjend = rida.split(" ")
    v�ljumisaeg = h_min(j�rjend[0])
    saabumisaeg = h_min(j�rjend[1])
    s�idu_kestvus = saabumisaeg - v�ljumisaeg
    hind = int(j�rjend[2])
    if s�idu_kestvus == l�him_kestvus or hind == madalaim_hind:
        j�rjekord.append(rida)
j�rjekord.sort()
for el in j�rjekord:
    print(el)
f.close()
