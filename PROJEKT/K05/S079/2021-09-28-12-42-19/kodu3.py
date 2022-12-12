def moos(suur, väike, kg):
    karpide_arv = 0
    suur_karp = suur
    väike_karp = väike
    kaal = kg
    if kaal <= 0:
        return karpide_arv
    if suur*5 + väike < kaal:
        return -1
    while suur_karp > 0:
        karpide_arv += 1
        kaal -= 5
        suur_karp -= 1
        if kaal < 5:
            break
    if kaal == 0:
        return karpide_arv 
    if väike_karp >= kaal:
        karpide_arv += kaal
    else:
        return -1
    return karpide_arv