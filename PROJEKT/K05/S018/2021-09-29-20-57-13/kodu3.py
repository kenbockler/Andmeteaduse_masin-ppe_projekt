def moos(s, v, m):
    v�ike = int(v)
    suur = int(s)
    mass = int(m)
    karp = 0
    kogu_v = suur*5 + v�ike
    while True:
        if mass > kogu_v or (mass < 5 and mass > v�ike):
            karp = -1
            break
        else:
            if mass >= 5 and suur > 0:
                karp += 1
                suur -= 1
                mass -= 5
            elif (mass < 5 or suur == 0) and mass >= 1 and v�ike > 0:
                karp += 1
                v�ike -= 1
                mass -= 1
            else:
                break
    return(karp)