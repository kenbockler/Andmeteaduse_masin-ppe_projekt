fail = input("Sisesta faili nimi: ")
fail = "s�iduplaan.txt"
f = open("s�iduplaan.txt", encoding = "UTF-8")
l�plik = []
tervik = []
for rida in f:
    j�rjend = rida.strip().split(" ")
    tervik.append(j�rjend)
print("Esimesest linnast teise s�itmiseks v�iksid kaaluda j�rgmisi busse:")
for i in range(len(tervik)):
    algus1 = tervik[i][0].split(":")
    l�pp1 = tervik[i][1].split(":")
    algustunnid1 = int(algus1[0])
    algusminutid1 = int(algus1[1])
    l�pptunnid1 = int(l�pp1[0])
    l�ppminutid1 = int(l�pp1[1])
    alguskoos1 = algustunnid1 + algusminutid1/60
    l�ppkoos1 =l�pptunnid1 + l�ppminutid1/60
    hind1 = float(tervik[i][2])
    for j in range(len(tervik)):
        algus2 = tervik[j][0].split(":")
        l�pp2 = tervik[j][1].split(":")
        algustunnid2 = int(algus2[0])
        algusminutid2 = int(algus2[1])
        l�pptunnid2 = int(l�pp2[0])
        l�ppminutid2 = int(l�pp2[1])
        alguskoos2 = algustunnid2 + algusminutid2/60
        l�ppkoos2 =l�pptunnid2 + l�ppminutid2/60
        hind2 = float(tervik[j][2])
        if alguskoos1 < alguskoos2 and l�ppkoos1 > l�ppkoos2 and hind1 > hind2:
            break
        if j == (len(tervik)-1):
            l�plik.append(tervik[i])
            continue
for a in range(len(l�plik)-1):
    for b in range(a+1, len(l�plik)):
        if l�plik[a] > l�plik[b]:
            l�plik[a], l�plik[b] = l�plik[b], l�plik[a]
for element in l�plik:
    s�ne = " ".join(element)
    print(s�ne)
    