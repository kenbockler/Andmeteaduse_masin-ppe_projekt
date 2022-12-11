eesnimi = input("Eesnimi: ")
perenimi = input("Perenimi: ")
nimi = eesnimi +"." + perenimi
kasutaja = nimi.lower().replace("õ","o").replace("ä","a").replace("ö","o").replace("ü","u")
print(kasutaja)