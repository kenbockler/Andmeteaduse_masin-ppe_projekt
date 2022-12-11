def poisse_ja_tüdrukuid(järjend):
    tüdrukuid = 0
    poisse = 0
    for sõne in järjend:
        sõne = sõne.strip()
        sugu = sõne[len(sõne)-1]
        if sugu == "T":
            tüdrukuid += 1
        else:
            poisse += 1
    return (poisse, tüdrukuid)