def auto_hind(alghind, aastad):
    if aastad == 0:
        return alghind
    else:
        return auto_hind(round((alghind * 0.8), 2), aastad - 1)