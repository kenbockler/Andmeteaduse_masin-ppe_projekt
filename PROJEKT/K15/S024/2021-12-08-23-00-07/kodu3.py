fail = input("Sisesta failinimi: ")
f = open(fail)
print("Esimesest linnast teise s�itmiseks v�iksid kaaluda j�rgmisi busse: ")
j�r = []
for rida in f:
    rida = rida.strip().split(" ")
    j�r.append(rida)
uus_j�r = []
for i in range(len(j�r)):
    for j in range(len(j�r)):
        if j�r[j][0] > j�r[i][0] and j�r[i][1] > j�r[j][1] and float(j�r[i][2]) > float(j�r[j][2]):
            if j�r[i] not in uus_j�r:
                uus_j�r.append(j�r[i])
for el in uus_j�r:
    j�r.remove(el)
for i in range(len(j�r)):
    varaseima_indeks = i
    for j in range(i+1, len(j�r)):
        if j�r[j][0] < j�r[i][0]:
            varaseima_indeks = j
    if i != varaseima_indeks:
        j�r[i], j�r[varaseima_indeks] = j�r[varaseima_indeks], j�r[i]
for i in range(len(j�r)):
    print(" ".join(j�r[i]))
f.close()
