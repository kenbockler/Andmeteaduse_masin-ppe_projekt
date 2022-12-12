'''-- Kodutöö nr. 15 - 1. Regulaaravaldis --'''
import re
f = open("aadressid.txt")
muster = r"~\S+"
for rida in f:
    if re.search("(https?)://(www)?.?(ut.ee)/~", rida):
        rida = rida.split("/")
        for r in rida:
            kasutajanimi = re.findall(muster, r)
            if kasutajanimi:
                print(kasutajanimi[0].lstrip("~"))
f.close()