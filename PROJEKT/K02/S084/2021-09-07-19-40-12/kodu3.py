eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")
kasutajanimi = eesnimi.lower() + "." + perenimi.lower()
kasutajanimi = kasutajanimi.replace("õ","o").replace("ä","a").replace("ü","u").replace("ö","o")
print(kasutajanimi)