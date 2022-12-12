failinimi = input("Sisesta failinimi: ")
f = open(failinimi)
bussid = []
for rida in f:
    rida = rida.strip().split()
    bussid.append(rida)
f.close()
bussid.sort(reverse = True)
bussid2 = []
for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if (buss[0] < buss2[0]) and (buss[2] > buss2[2]) and (buss[1] > buss2[1]):
            sobib = False
    bussid2.append(sobib)
for i in range(len(bussid2)):
    if bussid2[i] == False:
        del bussid[i]
    else:
        pass
bussid3 = []
for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if (buss[0] < buss2[0]) and (buss[2] > buss2[2]) and (buss[1] > buss2[1]):
            sobib = False
    bussid3.append(sobib)
for i in range(len(bussid3)):
    if bussid3[i] == False:
        del bussid[i]
    else:
        pass
bussid.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in range(len(bussid)):
       print(f'{bussid[i][0]} {bussid[i][1]} {bussid[i][2]}')
