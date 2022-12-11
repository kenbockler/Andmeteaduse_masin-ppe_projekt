def tähednumbrid(parool):
    tähestik = "ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXYabcdefghijklmnopqrsšzžtuvwõäöüxy"
    numbrid = "0123456789"
    sis_tähti = False
    sis_numbreid = False
    for täht in tähestik:
        if täht in parool:
            sis_tähti = True
            break
    for number in numbrid:
        if number in parool:
            sis_numbreid = True
            break
    return sis_numbreid and sis_tähti
def vaeseMeheKrüptograafia(parool):
    uus = ""
    for i in range(len(parool)):
        uus += parool[-(i+1)]
    return uus
kasutajanimi = input("Sisestage kasutajanimi: ")
kontroll = False
parool = ""
while not kontroll:
    parool = input("Sisestage parool: ")
    parool_verify = input("Sisestage parool uuesti: ")
    if not parool == parool_verify:
        print("Paroolid ei ühti. Proovige uuesti.")
    elif not (len(parool) >= 8):
        print("Parool peab olema vähemalt 8 tähemärgi pikkune.")
    elif not tähednumbrid(parool):
        print("Parool peab sisaldama tähti ja numbreid.")
    else:
        kontroll = True
kasutajad = open("users.txt", "a")
krüptoParool = vaeseMeheKrüptograafia(parool)
kasutajad.write(f"{kasutajanimi}:{krüptoParool}\n")
kasutajad.close()
