def moos(s_karbid, v_karbid, moos_kg):
    kasutatud_karbid = 0
    while s_karbid > 0 and moos_kg >= 5:
        s_karbid -= 1
        moos_kg -= 5
        kasutatud_karbid += 1
    if moos_kg > v_karbid:
        return -1
    while v_karbid > 0 and moos_kg > 0:
        v_karbid -= 1
        moos_kg -= 1
        kasutatud_karbid += 1
    return(kasutatud_karbid)
print(moos(5, 1, 9))