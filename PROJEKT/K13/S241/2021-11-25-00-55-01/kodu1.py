def auto_hind(hind, aastad):
    if aastad <= 0:
        return print(round(hind, 2))
    else:
        auto_hind(0.8*hind, aastad - 1)
auto_hind(1000,2.2)