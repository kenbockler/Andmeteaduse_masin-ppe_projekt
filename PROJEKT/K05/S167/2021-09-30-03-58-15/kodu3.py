def moos(x, y, z):
    suurkast=5
    väikekast=1
    koguskokku=0
    if z > 0:
        for i in range(0, z, 5):
            n = i
        if x == 1 and z == 5:
            n = 5
        suuredkastid = n/5
        if suuredkastid > x:
            suuredkastid = x
        jääk = z-suuredkastid*suurkast
        if jääk > y:
            jääk = y
        koguskokku = int(suuredkastid + jääk)
        kontroll = jääk*väikekast + suuredkastid*suurkast
        if kontroll < z:
            koguskokku = -1
    elif z == 0:
        koguskokku = 0
    else: koguskokku = -1
    return koguskokku
print(moos(1, 2, 0))