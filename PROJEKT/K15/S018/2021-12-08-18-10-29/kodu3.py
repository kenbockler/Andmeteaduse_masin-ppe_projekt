f_n = str(input("Sisesta s�iduplaanide faili nimi: "))
def number(kell):
    kell = kell.split(":")
    return int(kell[0]), int(kell[1])
def printer(rida):
    for el in rida:
        print(el, end = " ")
    print()
uus_j = []
with open(f_n, "r", encoding="UTF-8") as f:
    j�r = []
    for rida in f:
        rida = rida.strip().split(" ")
        j�r.append(rida)
n = len(j�r)
for i in range(n):
    v�ltund_1, v�lmin_1 = number(j�r[i][0])
    saabtund_1, saabmin_1 = number(j�r[i][1])
    hind_1 = int(j�r[i][2])
    for j in range(n):
        v�ltund_2, v�lmin_2 = number(j�r[j][0])
        saabtund_2, saabmin_2 = number(j�r[j][1])
        hind_2 = int(j�r[j][2])
        if v�ltund_1 < v�ltund_2:
            if saabtund_1 > saabtund_2:
                if hind_1 > hind_2:
                    uus_j.append(j�r[i])
                    break
            elif saabtund_1 == saabtund_2:
                if saabmin_1 > saabmin_2:
                    if hind_1 > hind_2:
                        uus_j.append(j�r[i])
                        break
        elif v�ltund_1 == v�ltund_2:
            if v�lmin_1 < v�lmin_2:
                if saabtund_1 > saabtund_2:
                    if hind_1 > hind_2:
                        uus_j.append(j�r[i])
                        break
                elif saabtund_1 == saabtund_2:
                    if saabmin_1 > saabmin_2:
                        if hind_1 > hind_2:
                            uus_j.append(j�r[i])
                            break
for el in uus_j:
    j�r.remove(el)
n = len(j�r)
for i in range(n-1):
        for j in range(n-i-1):
            tund_1, min_1 = number(j�r[j][0])
            tund_2, min_2 = number(j�r[j+1][0])
            if tund_1 > tund_2:
                j�r[j], j�r[j+1] = j�r[j+1], j�r[j]
            elif tund_1 == tund_2:
                if min_1 > min_2:
                    j�r[j], j�r[j+1] = j�r[j+1], j�r[j]
print("Esimesest linnast teise s�itmiseks v�id kaaluda j�rgmisi busse:")
for el in j�r:
    printer(el)