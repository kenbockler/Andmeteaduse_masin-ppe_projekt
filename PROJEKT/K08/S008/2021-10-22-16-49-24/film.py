fail = open("filmid.txt", "r", encoding= "UTF-8")
nimed = str()
žanrid = str()
fjärjend = []
fjärjend2 = []
for rida in fail: 
    järjend = rida.strip().split(" - ")
    fjärjend.append(järjend[0])
    fjärjend.append(järjend[1])
def loetleFilmid(žanrid):
   i = 0
   tagastavj =[]
   while i <len(fjärjend):
       if fjärjend[i+1] == žanrid:
           tagastavj.append(fjärjend[i])
       i +=2
   return tagastavj
print (loetleFilmid("multikas"))
fail.close()
nimi =input("Sisesta uue filmi nimi: ")
žanr = input("Sisesta uue filmi žanr: ")
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding= "UTF-8")
    fail.write("\n" + nimi + " - " + žanr)
    fjärjend.append(nimi)
    fjärjend.append(žanr)
    fail.close()
lisaFilm(nimi, žanr)
nimi2 = input("Kirjuta filmi nimi, mida soovid kustutada: ")
def kustutaFilm (nimi2):
    i = 0
    fail = open("filmid.txt", "w", encoding= "UTF-8")
    while i < len(fjärjend):
        if fjärjend[i] != nimi2:
            fail.write(fjärjend[i] + " - " + fjärjend[i+1] + "\n")
        i +=2
    fail.close() 
kustutaFilm(nimi2)                  