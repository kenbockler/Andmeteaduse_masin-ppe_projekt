enimi = input("Palun sisesta oma eesnimi ja vajuta ENTER: ")
pnimi = input("Palun sisesta oma perekonnanimi ja vajuta ENTER: ")
kasutajanimi = enimi.lower().replace('�','a').replace('�','o').replace('�','o').replace('�','u')+'.'+pnimi.lower().replace('�','a').replace('�','o').replace('�','o').replace('�','u')
print("Teie kasutajanimi on: " + kasutajanimi)
