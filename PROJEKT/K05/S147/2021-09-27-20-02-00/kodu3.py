def moos(suured,väikesed,kogus):
    if kogus <= suured*5+väikesed:
        if kogus//5 >= suured:
            karpe_kokku = suured
            jääk = int(kogus-(karpe_kokku*5))
            if väikesed >= jääk:
                karpe_kokku += jääk
                return karpe_kokku
            else:
                return -1
        else:
            karpe_kokku = kogus//5
            jääk = int(kogus-karpe_kokku*5)
            if väikesed >= jääk:
                karpe_kokku += jääk
                return karpe_kokku
            else:
                return -1
    else:
        return -1
print(moos(12,8,68))