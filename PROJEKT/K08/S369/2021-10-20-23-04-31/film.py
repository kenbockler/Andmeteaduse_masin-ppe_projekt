def loetleFilmid(žanr):
    f = open('filmid.txt')
    filmid = []
    for line in f:
        if line.strip().split(' - ')[-1] == žanr:
            filmid.append(line.strip().split(' - ')[0])
    return(filmid)     
    f.close()
def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding="utf-8")
    f.write("\n")
    f.write(nimi+ ' - '+ žanr)
    f.close()
def kustutaFilm(nimi):
    with open('filmid.txt', 'r') as f:
        lines = f.readlines()
    with open('filmid.txt', 'w') as f:
        for line in lines:
            if line.strip().split(' - ')[0] != nimi:
                f.write(line)
    f.close()
