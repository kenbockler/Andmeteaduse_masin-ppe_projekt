'''Kirjuta funktsioon moos, mis võtab argumendiks kolm täisarvulist väärtust:
suurte karpide arvu;
väikeste karpide arvu;
keedetava moosi koguse kilogrammides.
Funktsioon tagastab karpide arvu, mida Emma moosi keetmiseks kasutab. 
Kui moosikogus antud karpidesse ei mahu, tagastab funktsioon arvu -1.'''
import math
def moos(suurte_arv, vaikeste_arv, kogus):
    karpi_kokku = 0
    ulejaanud_kogus = 0
    suurte_karpide_arv = math.floor(kogus/5)
    if suurte_arv >= suurte_karpide_arv:
        karpi_kokku += suurte_karpide_arv
        ulejaanud_kogus = kogus%5
    else:
        karpi_kokku += suurte_arv
        ulejaanud_kogus = kogus - (suurte_arv*5)
    if vaikeste_arv >= ulejaanud_kogus:
        karpi_kokku += ulejaanud_kogus
    else:
        return -1
    return karpi_kokku