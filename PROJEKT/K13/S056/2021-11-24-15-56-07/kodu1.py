def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return round(auto_hind(hind*0.8, aastad - 1), 2)