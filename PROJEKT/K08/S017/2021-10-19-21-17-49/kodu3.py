import film
def t��tleK�sk(k�su_t�his, j�rjend_k�su_argumentidega):
    if k�su_t�his == "K":
        �anr = j�rjend_k�su_argumentidega[0]
        print("V�imalikud filmid on:")
        j�rjend = film.loetleFilmid(�anr)
        i = 0
        for el in j�rjend:
            print(j�rjend[i])
            i += 1
        tagastus = True
    elif k�su_t�his == "L":
        nimi = j�rjend_k�su_argumentidega[1]
        �anr = j�rjend_k�su_argumentidega[0]
        film.lisaFilm(nimi, �anr)
        print("Film lisatud!")
        tagastus = True
    elif k�su_t�his == "V":
        nimi = j�rjend_k�su_argumentidega[0]
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        tagastus = True
    elif k�su_t�his == "E":
        tagastus = False
    return tagastus
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <�anr>")
print("Lisa film:   L <�anr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("L�peta:      E")
print("===")
while True:
    k�sk = input("> ")
    k�sk = k�sk.split(" ")
    k�su_t�his = k�sk[0]
    if k�su_t�his == "L":
        �anr = k�sk[1]
        nimi = " ".join(k�sk[2:])
        j�rjend_k�su_argumentidega = [�anr, nimi]
    elif k�su_t�his == "E":
       j�rjend_k�su_argumentidega = [""]
    else:
        muu = " ".join(k�sk[1:])
        j�rjend_k�su_argumentidega = [muu]
    vastus = t��tleK�sk(k�su_t�his, j�rjend_k�su_argumentidega)
    if vastus == False:
        break
