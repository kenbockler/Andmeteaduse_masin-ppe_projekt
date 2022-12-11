def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        if aastad > 0:
            uus_hind = round((hind * 80) / 100, 2)
            lõpp = round(auto_hind(uus_hind, aastad-1), 2)
        return lõpp
print(auto_hind(8000, 5))