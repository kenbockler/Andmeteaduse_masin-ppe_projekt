fail = str(input("Sisesta failinimi: "))
f = open(fail)
read = f.readlines()
f.close()
v�ljumine=[]
saabumine=[]
hind=[]
for rida in read:
    info = rida.split(" ")
    v�ljumine.append(info[0])
    saabumine.append(info[1])
    hind.append((info[-1]).strip('\n'))
def sobivaim(v�ljumine, saabumine, hind):
    for el in hind:
        if el == max(hind):
            indeks = hind.index(el)
            v�ljumine.pop(indeks)
            saabumine.pop(indeks)
            hind.pop(indeks)
    for el in v�ljumine:
        if el == max(v�ljumine):
            indeks = v�ljumine.index(el)
            v�ljumine.pop(indeks)
            saabumine.pop(indeks)
            hind.pop(indeks)
    for el in saabumine:
        if el == max(saabumine):
            indeks = saabumine.index(el)
            v�ljumine.pop(indeks)
            saabumine.pop(indeks)
            hind.pop(indeks)
print("Esimesest linnast teise s�itmiseks v�iksid kaaluda j�rgmisi busse:")
sobivaim(v�ljumine, saabumine, hind)
sobivaid = len(hind)
x = sobivaid
while x >= 0:
    print(str(v�ljumine[x-1]) + " " +str(saabumine[x-1]) +" " + str(hind[x-1]))
    x -= 1