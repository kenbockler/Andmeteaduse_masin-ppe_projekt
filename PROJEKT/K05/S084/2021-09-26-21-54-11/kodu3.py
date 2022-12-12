def moos(suur, vaike, kg):
    karpe=0
    while kg >= 5 and suur != 0:
        karpe+=1
        suur-=1
        kg-=5
    while kg >= 1 and vaike != 0:
        karpe+=1
        vaike-=1
        kg-=1
    if kg != 0:
        karpe = -1
    return karpe