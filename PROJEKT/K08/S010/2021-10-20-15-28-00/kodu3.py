from film import*
def t��tleK�sk(t�his, j�rjend):
    try:
        nimi=''
        �anr=''
        if t�his=='K':
            �anr=j�rjend[0]
            print('V�imalikud filmid on: ')
            for rida in loetleFilmid(�anr):
                print(rida)
            return bool(True)
        if t�his=='L':
            �anr=j�rjend[0]
            i=1
            nimiT=''
            while i < len(j�rjend):
                nimiT+=(j�rjend[i]+' ')
                i+=1
            nimi=' '.join(nimiT.split())
            try:
                lisaFilm(nimi, �anr)
                print('Film lisatud!')
            except:
                print('Filmi lisamine eba�nnestus!')
            return bool(True)
        if t�his=='V':
            nimiT=''
            i=0
            while i < len(j�rjend):
                nimiT+=(j�rjend[i]+' ')
                i+=1
            nimi=' '.join(nimiT.split())
            kustutaFilm(nimi)
            print('Film nimekirjast kustutatud!')
            print('Head vaatamist!')
            return bool(True)
        if t�his=='E':
            return bool(False)
    except:
        return bool(False)
while True:
    print('=== FILMIANDMEBAAS ===')
    print('Kuva filmid: K <�anr>')
    print('Lisa film:   L <�anr> <film>')
    print('Vaata filmi: V <filmi nimi>')
    print('L�peta:      E')
    print('===')
    sisend=input('')
    sisendlist=sisend.split(' ')
    t�his=sisendlist[0]
    j�rjend=[]
    for rida in sisendlist:
        if rida!='K' and rida!='L' and rida!='V' and rida!='E':
            j�rjend+=[rida]
    if t��tleK�sk(t�his, j�rjend)==False:
        break