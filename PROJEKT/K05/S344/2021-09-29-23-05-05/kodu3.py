import math
a = 0
b = 0
c = 0
def moos(a, b, c):
    if c == 0:
        return 0
    if a * 5 + b < c:
        return -1
    suured_karbid = math.floor(c / 5)
    if a < suured_karbid:
        suured_karbid = a
    väikeste_karpide_kogus = c - (5 * suured_karbid)
    arv = suured_karbid + väikeste_karpide_kogus
    if väikeste_karpide_kogus > b:
        return -1
    return arv
print(moos(2, 20, 25))
print(moos(0, 10, 7))
print(moos(2, 6, 14))
print(moos(3, 4, 8))
print(moos(1, 2, 10))
print(moos(5, 1, 9))