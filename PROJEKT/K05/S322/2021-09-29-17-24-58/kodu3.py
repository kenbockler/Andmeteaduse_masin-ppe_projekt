def moos(suured, väikesed, moosi_kg):
    suuri = suured
    allesolev_moos = moosi_kg
    karpe = 0
    while suuri > 0 and allesolev_moos >= 5:
        allesolev_moos -= 5
        suuri -= 1
        karpe += 1
    if väikesed < allesolev_moos:
        return -1
    while allesolev_moos > 0:
        allesolev_moos -= 1
        karpe += 1
    return karpe
