def loetleFilmid(žanr):
    filmid = []
    f = open('filmid.txt', 'r', encoding = 'UTF-8')
    for rida in f:
        rida = rida.strip().split(' - ')
        nimi = rida[0]
        teema = rida[1]
        if teema == žanr:
            filmid.append(nimi)
    return filmid
    f.close()
def lisaFilm(nimi, žanr):
    a = open('filmid.txt', 'a', encoding = 'UTF-8')
    a.write('\n' + nimi + ' - ' + žanr)
    a.close()
def kustutaFilm(nimed):
    r = open('filmid.txt', 'r', encoding = 'UTF-8')
    read = r.readlines()
    r.close()
    w = open('filmid.txt', 'w', encoding = 'UTF-8')
    for rida in read: 
        nimi_ja_žanr = rida.strip().split(' - ')
        nimi = nimi_ja_žanr[0]
        if nimi != nimed and rida != '':
            w.write(rida)
        if rida == '':
            w.write() 
    w.close()