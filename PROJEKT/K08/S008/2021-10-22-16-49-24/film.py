fail = open("filmid.txt", "r", encoding= "UTF-8")
nimed = str()
�anrid = str()
fj�rjend = []
fj�rjend2 = []
for rida in fail: 
    j�rjend = rida.strip().split(" - ")
    fj�rjend.append(j�rjend[0])
    fj�rjend.append(j�rjend[1])
def loetleFilmid(�anrid):
   i = 0
   tagastavj =[]
   while i <len(fj�rjend):
       if fj�rjend[i+1] == �anrid:
           tagastavj.append(fj�rjend[i])
       i +=2
   return tagastavj
print (loetleFilmid("multikas"))
fail.close()
nimi =input("Sisesta uue filmi nimi: ")
�anr = input("Sisesta uue filmi �anr: ")
def lisaFilm(nimi, �anr):
    fail = open("filmid.txt", "a", encoding= "UTF-8")
    fail.write("\n" + nimi + " - " + �anr)
    fj�rjend.append(nimi)
    fj�rjend.append(�anr)
    fail.close()
lisaFilm(nimi, �anr)
nimi2 = input("Kirjuta filmi nimi, mida soovid kustutada: ")
def kustutaFilm (nimi2):
    i = 0
    fail = open("filmid.txt", "w", encoding= "UTF-8")
    while i < len(fj�rjend):
        if fj�rjend[i] != nimi2:
            fail.write(fj�rjend[i] + " - " + fj�rjend[i+1] + "\n")
        i +=2
    fail.close() 
kustutaFilm(nimi2)                  