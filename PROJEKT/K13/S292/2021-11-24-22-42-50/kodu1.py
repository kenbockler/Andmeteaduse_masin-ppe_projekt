def auto_hind(hind, aastad):
    if aastad >= 1:
        return auto_hind(0.8*hind, aastad-1)
    else:
        return round(hind, 2)
print(auto_hind(6788.46, 2))