lahtefail = input('Sisesta lähtefaili nimi koos .txt: ')
sihtfail = input('Sisesta sihtfaili nimi koos .txt: ')
lahtef = open(lahtefail)
sihtf = open(sihtfail, 'w')
loehello = lahtef.read()
asendamisi = int(loehello.count('Hello'))
tekst = loehello.replace('Hello', 'Tere')
sihtf.write(tekst)
lahtef.close()
sihtf.close()
print(asendamisi)