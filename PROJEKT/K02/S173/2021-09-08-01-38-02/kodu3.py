nimi = input(str("Sisesta eesnimi:"))
pnimi = input(str("Sisesta perenimi:"))
a = nimi.lower() + "." + pnimi.lower()
if "ü" or "õ" or "ö" or "ä" in a:
    a = a.replace("ü", "u")
    a = a.replace("õ", "o")
    a = a.replace("ö", "o")
    a = a.replace("ä", "a")
    print(a)
else:
    print(a)