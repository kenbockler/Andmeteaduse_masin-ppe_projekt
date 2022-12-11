def loetleFilmid(zanr):
    f=open("filmid.txt", encoding = "utf-8")
    nimed=[]
    for line in f:
        rida=line.strip().split(" - ")
        if rida[-1] == str(zanr):
            nimed.append(rida[0])
    f.close()
    return nimed
def lisaFilm(nimi, zanr):
    f=open("filmid.txt", "a", encoding = "utf-8")
    f.write("\n" + nimi + " - " + zanr)
    f.close()
def kustutaFilm(film):
    f=open("filmid.txt", "r+", encoding = "utf-8")
    for line in f:
        rida=line.strip().split(" - ")
        if film not in rida:
            f.write(line)        
    f.close()