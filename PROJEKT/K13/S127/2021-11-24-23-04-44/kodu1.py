def auto_hind(hind, aastad):
    if aastad<=0:
        return hind
    else:
        uus_hind=round(hind*(1-(20/100)), 2)
        return auto_hind(uus_hind, aastad-1)
print(auto_hind(10000, 5))