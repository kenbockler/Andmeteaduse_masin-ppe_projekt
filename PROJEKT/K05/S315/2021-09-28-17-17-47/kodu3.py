def moos(suur, väike, kg):
    a = kg - 5*suur - väike
    i = 0
    x = 0
    if a > 0:
        return -1
    elif a < 0:
        while x < kg:
            if kg - x < 5 or suur == 0:
                if väike == 0:
                    return -1
                    break
                x += 1
                i += 1
                väike -= 1
            else:
                x += 5
                i += 1
                suur -= 1
        return i
    else:
        while x < kg:
            if kg - x < 5 or suur == 0:
                x += 1
                i += 1
            else:
                x += 5
                i += 1
                suur -= 1
        return i
        