from pykkar import *
laius = int(input("Sisestage seinata seinata maailma laius(>2): "))+2
pikkus = int(input("Sisestage maailma pikkus(>2):"))+2
laudalg = '
print("NB! Laua 0, 0 koordinaadiks peetakse ülemist vasakpoolset nurka(alati sein)\nX- ning y-telg suurenevad vastavalt paremale ning alla ")
pykkarx = int(input("Sisestage Pykkari alguspunkti abtsiss: "))
pykkary = int(input("Sisestage Pykkari alguspunkti ordinaat: "))
laud = laudalg[:pykkary*(laius+1)+pykkarx]+'>'+laudalg[pykkary*(laius+1)+pykkarx+1:]
create_world(laud)
while(not is_wall()):
    step()
right()
for i in range(4):
    while(not is_wall()):
        step()
    paint()
    right()
exitonclick()