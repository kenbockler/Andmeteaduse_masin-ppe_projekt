def loetleFilmid(teema):
    f=open("filmid.txt", encoding="UTF-8")
    nimi=[]
    i=0
    for rida in f:
        rida2=rida.replace("\n", "")
        järjend=rida2.split(" - ")
        if järjend[1]==teema:
            nimi+=järjend[0:1]
            i+=1
        else:
            continue
    return(nimi)
    f.close()
def lisaFilm(nimi,teema):
    f=open("filmid.txt", "r", encoding="UTF-8")
    sisu=f.read()
    f.close()
    fa=open("filmid.txt", "w", encoding="UTF-8")
    fa.truncate(0)
    fa.write(sisu.strip()+"\n" + nimi + " - " + teema + "\n")
    fa.close()
def kustutaFilm(nimi):
    f=open("filmid.txt", "r", encoding="UTF-8")
    read=f.readlines()
    f.close()
    fx=open("filmid.txt", "w", encoding="UTF-8")
    i=0
    for rida in read:      
        järjend=read[i].split(" - ")
        i+=1
        if järjend[0] !=nimi:
            fx.write(rida)
        else:
            continue
    f.close()