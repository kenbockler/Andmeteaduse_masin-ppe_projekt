def auto_hind(hind,aastad):
    if aastad == 0:
        return(round(hind,2))
    else:
        hind *= 0.8
        aastad -=1
        return auto_hind(hind,aastad)