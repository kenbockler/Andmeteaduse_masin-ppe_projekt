kodutee = int(input("Sisesta tee pikkus kilomeetrites: "))
taksohinnad = open("taksohinnad.txt", "r", encoding="UTF-8")
taksopakkujad = taksohinnad.readlines()
taksohinnad.close()
odavaim_pakkuja = ""
odavaim_hind = 2**63
for takso in taksopakkujad:
    pakkuja = takso.split(",")[0]
    sisseastumishind = float(takso.split(",")[1])
    kmhind = float(takso.split(",")[2])
    if sisseastumishind + kodutee * kmhind < odavaim_hind:
        odavaim_pakkuja = pakkuja
        odavaim_hind = sisseastumishind + kodutee * kmhind
print(f"Kõige odavam on {odavaim_pakkuja}.")