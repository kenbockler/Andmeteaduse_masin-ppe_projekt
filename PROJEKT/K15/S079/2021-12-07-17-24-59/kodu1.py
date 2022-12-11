import re
f = open("aadressid.txt")
print("Kasutajanimed on: ")
for rida in f:
    rida = rida.strip()
    nimi = re.search("://www.ut.ee/~[a-ü]", rida)
    if nimi != None:
        r1 = rida.split("/~")[1].split("/")[0]
        print(r1)
    else:
        pass
f.close()
