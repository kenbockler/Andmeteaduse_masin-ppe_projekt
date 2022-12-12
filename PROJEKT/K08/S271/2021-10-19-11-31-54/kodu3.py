from film import *
def töötleKäsk(symbol, argumendid=[]):
    if symbol == 'E':
        return False
    elif symbol == 'K':
        filmid = loetleFilmid(argumendid[0])
        if filmid == []:
            print('Sellest žanrist pole ühtegi filmi!')
        else:
            print('Võimalikud filmid on:')
            for film in filmid:
                print(film)
            return True
    elif symbol == 'L':
        lisaFilm(argumendid[1], argumendid[0])
        print('Film lisatud!')
        return True
    elif symbol == 'V':
        kustutaFilm(argumendid[0])
        print('''Film nimekirjast kustutatud!
Head vaatamist!''')
        return True
while True:
    print('''=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <žanr> <film>
Lõpeta:      E
===''')
    sisend = input()
    sisend_jarjendina = sisend.split()
    if len(sisend_jarjendina) != 1:
        argumendid = []
        argumendid.append(sisend_jarjendina[1])
        film = ''
        for i in range(len(sisend_jarjendina)):
            if i < 2:
                continue
            elif i == 2:
                film += sisend_jarjendina[i]
            else:
                film += ' ' + sisend_jarjendina[i]      
        argumendid.append(film)
    if töötleKäsk(sisend_jarjendina[0], argumendid):
        continue
    else:
        break