failinimi = input("Sisestage failinimi: ")
fail = open(failinimi)
j�rjend = []
uus_j�rjend=[]
for rida in fail:
    rida = rida.strip()
    rida = rida.split(" ")
    j�rjend.append(rida)
    uus_j�rjend.append(rida)
for i in range(len(j�rjend)):
    for j in range(len(j�rjend)):
       if (j�rjend[i][0] <= j�rjend[j][0] and j�rjend[i][1] >= j�rjend[j][1] and int(j�rjend[i][2]) > int(j�rjend[j][2])):
            uus_j�rjend.remove(j�rjend[i])
            break
for i in range(len(uus_j�rjend)-1):
    for j in range(len(uus_j�rjend)-1):
        if uus_j�rjend[j][0] > uus_j�rjend[j+1][0]:
            uus_j�rjend[j], uus_j�rjend[j+1] = uus_j�rjend[j+1], uus_j�rjend[j]
print("Esimesest linnast teise s�itmiseks v�iksid kaaluda j�rgmisi busse:")
for el in uus_j�rjend:
    print(el[0],el[1],el[2])
        