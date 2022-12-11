def poisse_ja_tüdrukuid(x):
    ennik = ()
    i = 0
    try:
        rida_osadeks = x[i]
        poisse = 0
        tüdrukuid = 0
        rida_osadeks_osadeks = []
        while i < len(x):
            rida_osadeks = x[i]
            i += 1
            rida_osadeks_osadeks += rida_osadeks.split(" ")
        for element in rida_osadeks_osadeks:
            if element == "P":
                poisse += 1
            elif element == "T":
                tüdrukuid += 1
        ennik += (poisse, tüdrukuid)
        return ennik
    except:
        ennik = (0,0)
        return ennik