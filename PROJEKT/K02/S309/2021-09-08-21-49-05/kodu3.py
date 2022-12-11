eesnimi = str(input("Palun sisestage enda eesnimi:"));
perenimi = str(input("Palun sisestage enda perenimi:"));
kasutajanimi = eesnimi.lower() + "." + perenimi.lower();
kasutajanimi = kasutajanimi.replace('ü','u');
kasutajanimi = kasutajanimi.replace('õ','o');
kasutajanimi = kasutajanimi.replace('ö','o');
kasutajanimi = kasutajanimi.replace('ä','a');
print(kasutajanimi);