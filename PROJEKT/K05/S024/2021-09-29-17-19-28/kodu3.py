suurte_kaal = 5
v�ikeste_kaal = 1
def moos(suured_karbid, v�ikesed_karbid, kogus):
    kasutatud_suured = 0
    kasutatud_v�ikesed = 0
    kasutatud_karbid = kasutatud_suured + kasutatud_v�ikesed
    while (kogus - suurte_kaal)>= 0 and suured_karbid > 0:
        kogus -= suurte_kaal
        suured_karbid -= 1
        kasutatud_suured += 1
        if kogus == 0:
            return kasutatud_suured
        elif v�ikesed_karbid >= kogus:
            kasutatud_karbid = kasutatud_suured + kogus
            return kasutatud_karbid
    else:
        if kogus == 0:
            return 0
        else:
            return -1
    