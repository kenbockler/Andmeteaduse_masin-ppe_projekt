def moos(suured_karbid, v�iksed_karbid, moos_kg):
    kasutatud_karbid = 0
    if moos_kg/(suured_karbid*5 + v�iksed_karbid) != int() :
        return(-1)
    else:
        while suured_karbid>0 and suured_karbid*5 <= moos_kg:
            moos_kg = moos_kg-5
            suured_karbid = suured_karbid - 1
            kasutatud_karbid += 1
        while v�iksed_karbid>0 and v�iksed_karbid <= moos_kg:
            moos_kg -= 1
            v�iksed_karbid -= 1
            kasutatud_karbid += 1
        return (kasutatud_karbid)
