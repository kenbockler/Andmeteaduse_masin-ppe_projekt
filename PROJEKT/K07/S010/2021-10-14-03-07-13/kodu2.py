teepikkus=float(input('Sisesta tee pikkus kilomeetrites: '))
f=open('taksohinnad.txt', encoding='UTF-8')
hind=0
hinnad=[]
nimed=[]
for rida in f:
    hinnad.append(float((rida.strip()).split(',')[-2])+float((rida.strip()).split(',')[-1])*teepikkus)
    nimed.append((rida.strip()).split(',')[0])
try:
    v�ikseim=min(hinnad)
    v�ikseim_indeks=hinnad.index(v�ikseim)
    v�ikseim_nimi=nimed[v�ikseim_indeks]
    print('K�ige odavam on '+ v�ikseim_nimi +'.')
    f.close()
except:
    print('Viga failis!')
    f.close()