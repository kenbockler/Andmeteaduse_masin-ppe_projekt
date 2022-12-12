def moos(x, y, z):
    kasutatud_karpide_arv = 0
    if z > 0:
        if x > 0:
            while z >= 5 and x > 0:
                if z - 5 >= 0:
                    z -= 5
                    x -= 1
                    kasutatud_karpide_arv += 1
            if z == 0:
                return kasutatud_karpide_arv
            if y >= z and y!=0 :
                kasutatud_karpide_arv += z
                return kasutatud_karpide_arv
            else:
                return -1
        else:
            if y == 0:
                return -1
            else:
                if y >= z and y!=0:
                    kasutatud_karpide_arv += z
                    return kasutatud_karpide_arv
                else:
                    return -1
    else:
        return 0