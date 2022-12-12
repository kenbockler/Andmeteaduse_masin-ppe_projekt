def moos(suured_karbid,väikesed_karbid,moosi_kogus):
    mitu_karpi = (moosi_kogus // 5) 
    if mitu_karpi > suured_karbid:
        mitu_karpi = suured_karbid
    jääk = moosi_kogus - (mitu_karpi * 5)
    if (moosi_kogus - mitu_karpi * 5) > väikesed_karbid:
        tagastan = -1
    else:
        mitu_karpi = mitu_karpi + jääk
        tagastan = mitu_karpi
    return tagastan
