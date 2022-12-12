teepikkus = float(input('Kui pikk on teie teekond kilomeetrites?'))
taksonimed = []
sõiduhinnad = []
def madalam_hind():
    madalam = min(sõiduhinnad)
    indeks = sõiduhinnad.index(madalam)
    return taksonimed[indeks]
h1 = open('taksohinnad.txt')
for line in h1:
    hinnad = line.split(",")
    taksonimed.append(hinnad[0])
    sissehind = float(hinnad[1].strip())
    kmhind = float(hinnad[2].strip())
    sõiduhinnad.append(sissehind + kmhind*teepikkus)
print('Kõige odavam on', madalam_hind())
    