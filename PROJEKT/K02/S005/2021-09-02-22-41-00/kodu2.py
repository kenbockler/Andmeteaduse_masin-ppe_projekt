from math import ceil
total_dist = int(input("Kogupikkus?"))
dist_between_poles = int(input("Postidevaheline kaugus?"))
poles = total_dist / dist_between_poles
poles_ceil = 1 + ceil(poles)
if poles_ceil < 2:
    poles_ceil = 2
if poles < 2:
    print(poles)
print(poles_ceil)