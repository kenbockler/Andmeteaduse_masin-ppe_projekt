def loetleFilmid(žanr):
    f=open('filmid.txt', encoding= 'UTF-8')
    read=f.readlines()
    nimed=[]
    for i in range (len(read)):
        element= read[i].split(' - ')
        nime_el= element[0]
        žanri_el= element[1].strip('\n')
        if žanr == žanri_el:
            nimed= nimed + [nime_el]
    f.close()
    return nimed
def lisaFilm (nimi, žanr):
    f= open('filmid.txt','a',encoding= 'UTF-8')
    sisu= ('\n'+nimi+' - '+žanr+'\n')
    f.write(sisu)
    f.close()
def kustutaFilm (nimi):
    f=open('filmid.txt', encoding= 'UTF-8')
    read=f.readlines()
    for i in range (len(read)):
        element= read[i].split(' - ')
        nime_el= element[0]
        if nime_el== nimi:
            nimekiri= read[:i]+read[(i+1):]
    f.close()
    f=open('filmid.txt','w',encoding= 'UTF-8')
    for i in range(len(nimekiri)):
        rida=(nimekiri[i])
        f.write(rida)
    f.close()
