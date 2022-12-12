suur_k = int(input("Sisestage suurte karpide arv: "))
väike_k = int(input("Sisestage väikeste karpide arv: "))
kogus = int(input("Sisestage moosi kogus (kilogrammides): "))
def moos(suur_k, väike_k, kogus):
    karpide_maht = (suur_k * 5) + (väike_k * 1)
    if kogus == 0:
        return 0
    elif karpide_maht < kogus:
        return -1
    elif (suur_k * 5) / kogus != (suur_k * 5) // kogus and väike_k < kogus % 5:
        return -1
    elif suur_k == 0:
        vaja_väikeseid = väike_k - (väike_k - kogus)
        return vaja_väikeseid
    elif väike_k == 0:
        vaja_suuri = kogus // (suur_k * 5)
        return vaja_suuri
    else:
        vaja_suuri = 0
        while vaja_suuri < suur_k and kogus > 5:
            vaja_suuri += 1
            kogus -= 5
        vaja_väikeseid = 0
        while vaja_väikeseid < väike_k and kogus > 0:
            kogus -= 1
            vaja_väikeseid += 1
        kokku = vaja_väikeseid + vaja_suuri
        return kokku
print(moos(suur_k, väike_k, kogus))