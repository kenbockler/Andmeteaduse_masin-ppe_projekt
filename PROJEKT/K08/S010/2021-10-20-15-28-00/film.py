def loetleFilmid(�anr):
    f=open('filmid.txt', encoding='UTF-8')
    sisu=f.readlines()
    filmidelist=[]
    for element in sisu:
        if �anr in element.strip():
            filmidelist+=[element.split(' - ')[0]]
    f.close()
    return filmidelist
def lisaFilm(nimi, �anr):
    a=open('filmid.txt', encoding='utf-8')
    sisu=a.read()
    a.close()
    f=open('filmid.txt', mode='w', encoding='utf-8')
    f.write(sisu+'\n'+nimi+' - '+�anr + '\n')
    f.close()
def kustutaFilm(nimi):
    a=open('filmid.txt', encoding='utf-8')
    sisulist=a.readlines()
    �ige_sisulist=[]
    for element in sisulist:
        if nimi not in element.strip():
            �ige_sisulist+=[element]
    a.close()
    f=open('filmid.txt', mode='w', encoding='utf-8')
    for element1 in �ige_sisulist:
        f.write(element1)
    f.close()
    