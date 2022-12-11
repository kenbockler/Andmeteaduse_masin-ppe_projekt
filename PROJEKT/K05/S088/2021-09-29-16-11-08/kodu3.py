def moos(a, b, c):
    smaht = a * 5
    if c % 5 - (int(c % 5)) == 0 and smaht + b >= c and c % 5 <= b:
        if smaht >= c:
            s = int(c / 5)
            v = c % 5
            return s+v
        elif smaht < c:
            j = c - smaht
            m = int((c - j) / 5)
            return j + m
    else:
        return -1