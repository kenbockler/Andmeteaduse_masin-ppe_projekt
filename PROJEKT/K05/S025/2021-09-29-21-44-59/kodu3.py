def moos(suur, väike, kogus):
    kasutatud = 0
    if kogus > 5 * suur + väike:
        return -1
    while kogus >= 5:
        if suur == 0:
            break
        kogus -= 5
        suur -= 1
        kasutatud += 1
    while kogus > 0:
        if väike == 0:
            return -1
        kogus -= 1
        väike -= 1
        kasutatud += 1
    return kasutatud
moos(2, 20, 25)