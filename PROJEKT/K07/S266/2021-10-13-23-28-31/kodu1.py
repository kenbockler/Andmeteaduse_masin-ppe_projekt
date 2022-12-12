def poisse_ja_tüdrukuid(jrd):
    poisse = 0
    tüdrukuid = 0
    for rida in jrd:
        lisa = rida.split(" ")
        if "P" in lisa:
            poisse += 1
        elif "T" in lisa:
            tüdrukuid += 1
    stat = (poisse, tüdrukuid)
    return stat