eesnimi = input("Mis on Teie eesimi? ")
perenimi = input ("Mis on Teie perekonnanimi? ")
kasunimi = (eesnimi.replace("�", "u").replace("�", "u").replace("�", "o").replace("�", "o").replace("�", "a").replace("�", "a").replace("�", "o").replace("�", "o").lower() + "." + perenimi.replace("�", "u").replace("�", "u").replace("�", "o").replace("�", "o").replace("�", "a").replace("�", "a").replace("�", "o").replace("�", "o").lower())
print ("Teie kasutajanimi on:", kasunimi)