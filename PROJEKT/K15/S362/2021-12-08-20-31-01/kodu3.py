failinimi=input("Sisesta failinimi: ")
f=open(failinimi, "r", encoding="UTF-8")
listide_list=[]
uus_list=[]
uus_list2=[]
for rida in f:
    rida=rida.strip().split(" ")
    listide_list+=[rida]
for i in range(len(listide_list)):
    sobivus=True
    for j in range(len(listide_list)):
        if listide_list[i][2]>listide_list[j][2] and  listide_list[i][0]<listide_list[j][0] and listide_list[i][1]>listide_list[j][1]:
            sobivus=False
    if sobivus==True:
        uus_list+=[listide_list[i]]
for i in range(len(uus_list)):
    for j in range(i+1, len(uus_list)):
        if uus_list[i][0]>uus_list[j][0]:
            uus_list[i],uus_list[j]=uus_list[j],uus_list[i]
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for el in uus_list:
    print(" ".join(el))
    