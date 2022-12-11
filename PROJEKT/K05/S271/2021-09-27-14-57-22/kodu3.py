def moos(suur, väike, kogus):
    karpe = 0
    while True:
        if kogus == 0:
            return karpe
        if suur > 0:
            if kogus % 5 == 0:
                kogus -= 5
                suur -=1
                karpe += 1
                continue
        if väike > 0:
            kogus -= 1
            väike -= 1
            karpe += 1
        else:
            return -1