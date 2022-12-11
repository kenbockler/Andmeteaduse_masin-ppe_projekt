def seosta_lapsed_ja_vanemad(laste_fail, nimed):
    f1=open(laste_fail, "r", encoding="UTF-8")
    f2=open(nimed, "r", encoding="UTF-8")
    isikukoodid=[]
    sõnastik={}
    sõnastik2={}
    for rida in f2:
        rida=rida.strip()
        rida_list2=rida.split(" ")
        nimi=rida_list2[1]+' '+rida_list2[2]
        sõnastik[rida_list2[0]]=nimi
    for rida in f1:
        rida=rida.strip()
        rida_list1=rida.split(" ")
        if sõnastik[rida_list1[1]] not in sõnastik2:
            sõnastik2[sõnastik[rida_list1[1]]]={sõnastik[rida_list1[0]]}
        else:
            sõnastik2[sõnastik[rida_list1[1]]].add(sõnastik[rida_list1[0]])
    f1.close()
    f2.close()
    return sõnastik2
laste_fail="lapsed.txt"
nimed="nimed.txt"
sõnastik2=seosta_lapsed_ja_vanemad(laste_fail, nimed)
for el in sõnastik2:
    print(str(el)+': '+str(', '.join(list(sõnastik2[el]))))
 