def auto_hind(hind, aastad):
    if aastad < 1:
        return hind
    else:
        vaartus = round(hind * 0.8, 2)
        return auto_hind(vaartus, aastad - 1 )