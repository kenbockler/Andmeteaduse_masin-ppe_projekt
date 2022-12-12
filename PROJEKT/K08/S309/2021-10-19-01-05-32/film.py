def loetleFilmid(genre):
    try:
        films = []
        file = open("filmid.txt", "r", encoding="UTF-8")
        for line in file:
            currentline = line.split(" - ")
            if currentline[1].strip() == genre:
                films.append(currentline[0])
        file.close()
        return films
    except Exception as e:
        print(e)
def lisaFilm(name, genre):
    try:
        file = open("filmid.txt", "a", encoding="UTF-8")
        file.write(f"\n{name} - {genre}")
        file.close()
    except Exception as e:
        print(e)
def kustutaFilm(name):
    try:
        file = open("filmid.txt", "r", encoding="UTF-8")
        films = file.readlines()
        file.close()
        for film in films:
            if film.split(" - ")[0] == name:
                films.remove(film)
        file = open("filmid.txt", "w", encoding="UTF-8")
        length = len(films)
        for index,film in enumerate(films):
            if not index == length - 1:
                file.write(film)
            else:
                file.write(film.strip())
        file.close()
    except Exception as e:
        print(e)
