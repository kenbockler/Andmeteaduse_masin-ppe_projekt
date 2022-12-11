eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")
kombinatsioon = eesnimi.lower() + "." + perenimi.lower()
väljund = ""
for täht in kombinatsioon:
    if täht == "ö" or täht == "õ":
        väljund+="o"
    elif täht == "ü":
        väljund+="u"
    elif täht == "ä":
        väljund+="a"
    else:
        väljund+=täht
print(väljund)