def moos(suured_karbid, väiksed_karbid, moos_kg):
    suured_moosikarbid = moos_kg // 5
    kasutada_suuri = min(suured_karbid, suured_moosikarbid)
    väikseid_vaja = moos_kg - 5 * kasutada_suuri
    if väikseid_vaja <= väiksed_karbid:
        return(kasutada_suuri + väikseid_vaja)
    else:
        return -1
