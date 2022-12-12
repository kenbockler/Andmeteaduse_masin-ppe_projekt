import film
def töötleKäsk(käsu_tähis, järjend):
    if käsu_tähis == 'K':
        filmid = film.loetleFilmid(järjend)
        if len(filmid) == 0:
            print('Soovitud žanrist pole ühtegi filmi')
        else:
            print('Võimalikud filmid on: ')
            for i in filmid:
                print(i)
    elif käsu_tähis == 'L':
        žanr = järjend[0]
        nimi = järjend[1]
        film.lisaFilm(nimi, žanr)
        print('Film lisatud!')
    elif käsu_tähis == 'V':
        film.kustutaFilm(järjend)
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
    elif käsu_tähis == 'E':
        return False
    else:
        return True
print('=== FILMIANDMEBAAS ===')
print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')
print('===')
t = True
while t == True:
    sisestus = input('> ')
    argumendid = sisestus.split(' ', 1)
    if len(argumendid) == 1:
        t = töötleKäsk(sisestus, [])
    else:
        käsu_tähis = argumendid[0]
        järjendid = argumendid[1]
        if käsu_tähis == 'L':
            järjend = järjendid.split(' ', 1)
            töötleKäsk(käsu_tähis, järjend)
        else:
            töötleKäsk(käsu_tähis, järjendid)
