ees = input("Sisesta oma eesnimi")
pere = input("Sisesta oma perekonnanimi")
nimi = ees + "." + pere
print(nimi.replace('�', 'a').replace('�', 'o').replace('�', 'y').replace('�', 'o').lower())
