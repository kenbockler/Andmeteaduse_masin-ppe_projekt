from film import *
def t��tleK�sk(k�sk, j�r):
    if k�sk == 'E':
        return False
    elif k�sk == 'K':
        print('V�imalikud filmid on: ')
        for el in loetleFilmid(j�r[0]):
            print(el)
        return True
    elif k�sk == 'V':
        kustutaFilm(' '.join(j�r))
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
        return True
    elif k�sk == 'L':
        nimi = ' '.join(j�r[1:])
        zanr = j�r[0]
        lisaFilm(nimi, zanr)
        print('Film lisatud!')
        return True
    else:
        return False
print('Kuva filmid: K <�anr>')
print('Lisa film:   L <�anr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('L�peta:      E')
while True:
    sisend = input()
    i = sisend.find(' ')
    s�ne = sisend[:i].strip()
    j�rjend = sisend[i+1:].split()
    if sisend == 'E':
        break
    t��tleK�sk(s�ne, j�rjend)