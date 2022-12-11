eesnimi = input(str("Sisesta oma eesnimi: "))
perenimi = input(str("Sisesta oma perekonnanimi: "))
import unicodedata
bytes_eesnimi = unicodedata.normalize('NFD', eesnimi).encode('ascii', 'ignore')
norm_eesnimi = bytes_eesnimi.decode('ascii', 'ignore')
bytes_perenimi = unicodedata.normalize('NFD', perenimi).encode('ascii', 'ignore')
norm_perenimi = bytes_perenimi.decode('ascii', 'ignore')
print(norm_eesnimi.casefold() + "." + norm_perenimi.casefold())