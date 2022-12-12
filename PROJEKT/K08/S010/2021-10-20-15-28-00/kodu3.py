from film import*
def töötleKäsk(tähis, järjend):
    try:
        nimi=''
        žanr=''
        if tähis=='K':
            žanr=järjend[0]
            print('Võimalikud filmid on: ')
            for rida in loetleFilmid(žanr):
                print(rida)
            return bool(True)
        if tähis=='L':
            žanr=järjend[0]
            i=1
            nimiT=''
            while i < len(järjend):
                nimiT+=(järjend[i]+' ')
                i+=1
            nimi=' '.join(nimiT.split())
            try:
                lisaFilm(nimi, žanr)
                print('Film lisatud!')
            except:
                print('Filmi lisamine ebaõnnestus!')
            return bool(True)
        if tähis=='V':
            nimiT=''
            i=0
            while i < len(järjend):
                nimiT+=(järjend[i]+' ')
                i+=1
            nimi=' '.join(nimiT.split())
            kustutaFilm(nimi)
            print('Film nimekirjast kustutatud!')
            print('Head vaatamist!')
            return bool(True)
        if tähis=='E':
            return bool(False)
    except:
        return bool(False)
while True:
    print('=== FILMIANDMEBAAS ===')
    print('Kuva filmid: K <žanr>')
    print('Lisa film:   L <žanr> <film>')
    print('Vaata filmi: V <filmi nimi>')
    print('Lõpeta:      E')
    print('===')
    sisend=input('')
    sisendlist=sisend.split(' ')
    tähis=sisendlist[0]
    järjend=[]
    for rida in sisendlist:
        if rida!='K' and rida!='L' and rida!='V' and rida!='E':
            järjend+=[rida]
    if töötleKäsk(tähis, järjend)==False:
        break