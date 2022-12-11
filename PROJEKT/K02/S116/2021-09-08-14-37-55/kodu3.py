eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")
kasutaja = eesnimi.lower() + "." + perenimi.lower()
for i in kasutaja:
    if i == "õ" or i == "ö":
        i = "o"
    if i == "ü":
        i = "u"
    if i == "ä":
        i = "a"
print(kasutaja)