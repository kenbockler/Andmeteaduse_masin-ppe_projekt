def loetleFilmid(genre):
    f = open('filmid.txt', encoding='utf-8')
    all_movies = f.readlines()
    found_movies = []
    f.close()
    for i in range(len(all_movies)):
        if genre in all_movies[i]:
            found_movies.append(all_movies[i].split(' - ')[0])
    return found_movies
def lisaFilm(movie, genre):
    f = open('filmid.txt', 'a', encoding='utf-8')
    f.write('\n' + movie + ' - ' + genre)
    f.close()
def kustutaFilm(movie):
    f = open('filmid.txt', 'r', encoding='utf-8')
    all_movies = f.readlines()
    f.close()
    f = open('filmid.txt', 'w', encoding='utf-8')
    for i in all_movies:
        if not movie in i:
            f.write(i)
    f.close()