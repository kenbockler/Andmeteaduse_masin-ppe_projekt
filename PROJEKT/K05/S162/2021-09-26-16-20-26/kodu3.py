def moos(suur,väike,kogus):
    global karpe
    karpe=0
    while kogus>=5 and suur>0:
        kogus-=5
        suur-=1
        karpe+=1
    if väike>=kogus and kogus>=0:
        karpe+=kogus
        return karpe
    else:
        return -1
    