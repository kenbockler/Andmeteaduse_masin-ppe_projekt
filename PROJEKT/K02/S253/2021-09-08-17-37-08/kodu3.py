eesnimi = input("Sisestage oma eesnimi: ")
perenimi = input("Sisestage oma perenimi: ")
low_eesnimi = eesnimi.lower()
low_perenimi = perenimi.lower()
final_eesnimi = low_eesnimi.replace("õ", "o").replace("ö", "o").replace("ä","a").replace("ü","u")
final_perenimi = low_perenimi.replace("õ", "o").replace("ö", "o").replace("ä","a").replace("ü","u")
print(final_eesnimi + "." + final_perenimi)