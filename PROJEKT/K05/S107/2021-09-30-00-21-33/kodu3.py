suured_karbid = int(input("Sisesta suurte karpide arv: "))
väiksed_karbid = int(input("Sisesta väikeste karpide arv: "))
kogus = int(input("Sisesta moosi kogus: "))
def moos(suured_karbid, väikesed_karbid, kogus):
    karbid = 0
    suuri_saaks = kogus // 5
    if suuri_saaks > suured_karbid:
        karbid = suured_karbid
    else:
        karbid = suuri_saaks
    väikeseid_vaja = kogus - 5 * karbid
    if väikeseid_vaja > väikesed_karbid:
        return -1
    return karbid + väikeseid_vaja
print(moos(suured_karbid, väiksed_karbid, kogus))
        