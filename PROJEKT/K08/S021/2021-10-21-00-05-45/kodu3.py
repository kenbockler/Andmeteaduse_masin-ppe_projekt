import film
sisend = input(str("Sisestage k�sk ning t�hikuga eraldatud argumendid: "))
sisendj�rjend = sisend.split()
t�his = sisendj�rjend[0]
nimij�rjend = sisendj�rjend[1:]
def t��tleK�sk(t�his, j�rjend):
    if t�his == "K":
        �anr = nimij�rjend[0]
        tulemus = film.loetleFilmid(�anr)
        if tulemus == []:
            print("Failis pole otsitud �anrist �htegi filmi")
        else:
            print("V�imalikud filmid on:")
            i = 0
            while i < len(tulemus):
                kirjutatav = tulemus[i]
                i += 1
                print(kirjutatav)
            return True
    if t�his == "L":
        nimi = nimij�rjend[1] + nimij�rjend[2]
        �anr = nimij�rjend[0]
        film.lisaFilm(nimi, �anr)
        print("Film lisatud")
        return True
    if t�his == "V":
        nimi = " ".join(nimij�rjend)
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist")
        return True
    if t�his == "E":
        return False
t��tleK�sk(t�his, nimij�rjend)