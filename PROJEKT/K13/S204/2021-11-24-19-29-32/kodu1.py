def auto_hind(hind, aastad):
    if aastad < 1:
        return round(hind, 2)
    else:
        uus_hind = hind * (1-(20/100))
        uued_aastad = aastad - 1
        return auto_hind(uus_hind, uued_aastad)