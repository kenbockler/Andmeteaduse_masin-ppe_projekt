def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for element in järjend:
        if element[-1] == "P":
            poiste_arv += 1
        else:
            tüdrukute_arv += 1
    return (poiste_arv, tüdrukute_arv)