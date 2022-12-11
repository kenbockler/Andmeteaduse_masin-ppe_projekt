eesnimi = input("Sisestage eesnimi: ")
perenimi = input("Sisestage perenimi: ")
kogunimi = eesnimi.lower() + "."+ perenimi.lower()
if kogunimi.isascii() == False:
    if kogunimi.rfind('õ') != -1:
        kogunimi = kogunimi.replace("õ","o")
    if kogunimi.rfind('ö') != -1:
        kogunimi = kogunimi.replace("ö","o")
    if kogunimi.rfind('ä') != -1:
        kogunimi = kogunimi.replace("ä","a")
    if kogunimi.rfind('ü') != -1:
        kogunimi = kogunimi.replace("ü","u")
    else:
        kogunimi = kogunimi
print(kogunimi)
