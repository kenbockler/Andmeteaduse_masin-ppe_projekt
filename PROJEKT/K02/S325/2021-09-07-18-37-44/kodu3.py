eesn=str(input("Kirjuta oma eesnimi:"))
peren=str(input("Kirjuta oma perenimi:"))
eesn= eesn.replace("ü","u",)
eesn= eesn.replace("õ","o",)
eesn= eesn.replace("ö","o",)
eesn= eesn.replace("ä","a",)
peren= peren.replace("ü","u",)
peren= peren.replace("ä","a",)
peren= peren.replace("õ","o",)
peren= peren.replace("ö","o",)
print(str.lower(eesn)+"."+str.lower(peren))