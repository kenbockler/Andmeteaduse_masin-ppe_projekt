import copy
failinimi=input('Sisesta failinimi: ')
f=open(failinimi, encoding='utf-8')
bussid=[]
for rida in f:
    buss=rida.strip().split(' ')
    bussid+=[buss]
f.close()
print(bussid)
bussid_teisendatud=[]
for buss in bussid:
    aeg1=buss[0].split(':')
    teisendatudaeg1=int(aeg1[0])*60+int(aeg1[1])
    aeg2=buss[1].split(':')
    teisendatudaeg2=int(aeg2[0])*60+int(aeg2[1])
    aegade_vahe=teisendatudaeg2-teisendatudaeg1
    bussid_teisendatud.append([aegade_vahe, int(buss[2])])
print(bussid_teisendatud)
bussid_teisendatud2=copy.deepcopy(bussid_teisendatud)
def j�rjesta_punktid(p):
    for indeks in range(0, len(p)-1):
        v�him=indeks
        for j in range(indeks, len(p)):
            if p[j][1]<p[v�him][1]:
                v�him=j
            elif p[j][1]==p[v�him][1] and p[j][0]<p[v�him][0]:
                v�him=j            
        p[indeks], p[v�him]=p[v�him], p[indeks]
    return p
j�rjesta_punktid(bussid_teisendatud2)
indeksid=[]
for el in bussid_teisendatud2:
    �ige_indeks=bussid_teisendatud.index(el)
    indeksid.append(�ige_indeks)
print(indeksid)
loendur=0
for i in range(len(bussid)):
    indeks=indeksid[i]
    print(bussid[indeks])
    loendur+=1
    if loendur>=2:
        break