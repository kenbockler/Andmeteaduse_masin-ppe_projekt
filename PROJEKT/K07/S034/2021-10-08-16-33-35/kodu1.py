def poisse_ja_tüdrukuid(järjend):
    sõne = ""
    poiste_arv = 0
    tüdrukute_arv = 0
    for rida in järjend:
        sõne = rida[-1]
        if sõne == "P":
            poiste_arv += 1
        elif sõne == "T":
            tüdrukute_arv += 1
    return(poiste_arv, tüdrukute_arv)
