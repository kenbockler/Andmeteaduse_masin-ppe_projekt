def poisse_ja_tüdrukuid(nimed):
    poisse = 0
    tüdrukuid = 0
    for el in nimed:
        if el[-1] == "P":
            poisse += 1
        elif el[-1] == "T":
            tüdrukuid +=1
    return (poisse, tüdrukuid)