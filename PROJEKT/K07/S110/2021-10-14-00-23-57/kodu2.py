koju = float(input('Sisesta teepikkus kilomeetrites: '))
f = open('taksohinnad.txt')
sisu = f.readlines()
i = []
nimi = []
n = 0
for rida in sisu:
    rida = rida.strip()
    järjend = rida.split(',')
    if rida == '':
        break
    hind = float(järjend[1]) + koju * float(järjend[2])
    i += [hind]
odavaim = min(i)
print(nimi,odavaim)