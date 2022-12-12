def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return round(auto_hind(hind, aastad-1)*(1-20/100), 2)
