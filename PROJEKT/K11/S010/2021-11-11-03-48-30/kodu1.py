def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    f1=open(lastefail, encoding='utf-8')
    f2=open(nimedefail, encoding='utf-8')
    f1_vanematekoodid=[]
    f1_lastekoodid=[]
    for rida in f1:
        andmed1=rida.strip().split()
        f1_vanematekoodid+=[andmed1[0]]
        f1_lastekoodid+=[andmed1[1]]
    f1.close()
    f2_isikukoodid=[]
    f2_nimed=[]
    for rida in f2:
        andmed2=rida.strip().split(' ', 1)
        f2_isikukoodid+=[andmed2[0]]
        f2_nimed+=[andmed2[1]]
    f2.close()
    d2_isikukood_nimi={}
    for indeks in range(len(f2_isikukoodid)):
        d2_isikukood_nimi[f2_isikukoodid[indeks]]=f2_nimed[indeks]  
    tulemuss�nastik={}
    for indeks in range(len(f1_vanematekoodid)):
        if d2_isikukood_nimi[f1_lastekoodid[indeks]] not in tulemuss�nastik:
            tulemuss�nastik[d2_isikukood_nimi[f1_lastekoodid[indeks]]]=set()
            tulemuss�nastik[d2_isikukood_nimi[f1_lastekoodid[indeks]]].add(d2_isikukood_nimi[f1_vanematekoodid[indeks]])
        else:
            tulemuss�nastik[d2_isikukood_nimi[f1_lastekoodid[indeks]]].add(d2_isikukood_nimi[f1_vanematekoodid[indeks]])
    return tulemuss�nastik
s�nastik=seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for v�ti in s�nastik:
    if len(s�nastik[v�ti])==2:
        vanemad=[]
        for el in s�nastik[v�ti]:
            vanemad+=[el]
        print(v�ti+': '+vanemad[0]+', '+vanemad[1])
    else:
        vanem=''
        for el in s�nastik[v�ti]:
            vanem=el
        print(v�ti+': '+vanem )