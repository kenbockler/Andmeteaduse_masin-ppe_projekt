def poisse_ja_tüdrukuid(nimed):
    poisid = 0
    tüdrukud = 0
    for sugu in nimed:
        if sugu[-1] == "P":
            poisid += 1
        else:
            tüdrukud += 1
    return(poisid, tüdrukud)
nimed = ["Mati P", "Kati T", "Siim Aleksander P", "Juri P", "Veronika T"]
poisse_ja_tüdrukuid(nimed)
print(poisse_ja_tüdrukuid(nimed))
    