def moos(suured, väikesed, keedetav_moos):
    kasutatud = 0
    if keedetav_moos%1 != 0:
        return -1
    while keedetav_moos != 0:
        if suured > 0 and keedetav_moos >= 5:
            suured-=1
            kasutatud+=1
            keedetav_moos-=5
            continue
        elif väikesed > 0:
            väikesed-=1
            kasutatud+=1
            keedetav_moos-=1
            continue
        else:
            return -1
    return kasutatud
            