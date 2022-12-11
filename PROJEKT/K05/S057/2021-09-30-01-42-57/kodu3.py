from math import floor
def moos(suur, väike, kogus):
    if suur * 5 + väike * 1 >= kogus:
        skarbid = floor(kogus / 5)
        jääk = floor(kogus % 5)
        vkarbid = floor(jääk / 1) 
        if väike < vkarbid:
            return -1
        kokku = skarbid + vkarbid
        return kokku
    else:
        return -1