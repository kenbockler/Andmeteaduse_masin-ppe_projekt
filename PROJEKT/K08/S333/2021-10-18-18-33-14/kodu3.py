import film
def töötleKäsk(tähis,argument):
    if tähis== 'K':
        return film.loetleFilmid(argument[0])
    elif tähis== 'L':
        if len(argument)>1:
            argument= argument[0:1]+[' '.join(argument[1:])]
        film.lisaFilm(argument[1],argument[0])
    elif tähis== 'V':
        if len(argument)>1:
            argument= [argument[0]+' '+argument[1]]
        film.kustutaFilm(argument[0])
print('=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\n'+
          'Vaata filmi: V <filmi nimi>\nLõpeta:      E')
E=True
while E:
    sisend=input()
    sisend= sisend.split()
    if sisend[0]=='E':
        E= False
    elif sisend[0]== 'K':
        tulemus=töötleKäsk(sisend[0],sisend[1:])
        if tulemus==[]:
            print('Kahjuks antud žanrist filmi pakkuda pole, proovi uuesti!')
        else:
            print('Võimalikud filmid on:')
            for i in range(len(tulemus)):
                print(tulemus[i])
    elif sisend[0]== 'L':
        töötleKäsk(sisend[0],sisend[1:])
        print('Film lisatud!')
    elif sisend[0]== 'V':
        töötleKäsk(sisend[0],sisend[1:])
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
