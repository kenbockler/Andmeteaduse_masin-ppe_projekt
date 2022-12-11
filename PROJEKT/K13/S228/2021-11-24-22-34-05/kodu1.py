def auto_hind(hind, aastad):
    if aastad == 0:
        hind = round(hind, 2)
        return hind
    else:
        uus_hind = 0.8 * hind
        uus_hind = round(uus_hind, 2)
        return auto_hind(uus_hind, aastad - 1)