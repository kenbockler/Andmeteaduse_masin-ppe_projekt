def hinna_kalkulaator(a,b):
    hind= a+b*tee_pikkus
    return hind
nimed= []
sisseistumine= []
kilomeeter= []
arvutatud_hinnad= []
hinnad=open('taksohinnad.txt',encoding='UTF-8')
tee_pikkus= float(input('Sisesta tee pikkus kilomeetrites: '))
for rida in hinnad:
    rida= rida.strip('\n').split(',')
    nimed= nimed+ [rida[0]]
    sisseistumine= sisseistumine +[float(rida[1])]
    kilomeeter= kilomeeter+ [float(rida[2])]
hinnad.close()
i=0
while i< len(nimed):
    hind= hinna_kalkulaator(sisseistumine[i],kilomeeter[i])
    arvutatud_hinnad= arvutatud_hinnad + [hind]
    i+=1
i=0
for hind_min in arvutatud_hinnad:
    if hind_min == min(arvutatud_hinnad):
        print(' Kõige odavam on ',nimed[i], 'hinnaga',hind_min,'€.')
    else:
        i+=1
    