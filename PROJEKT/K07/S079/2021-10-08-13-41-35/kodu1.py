def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for i in järjend:
        if i[-1] == "P":
            poisse += 1
        if i[-1] == "T":
            tüdrukuid += 1
    kokku = (poisse, tüdrukuid)
    return kokku
