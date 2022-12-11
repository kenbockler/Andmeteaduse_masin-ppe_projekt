def seosta_lapsed_ja_vanemad(fail1, fail2):    
    sõnastik_nimed = {}
    with open(fail1) as fail_nimed:
        for rida in fail_nimed:
            (ik, nimi) = rida.strip().split(' ',1)
            sõnastik_nimed[ik] = nimi
    sõnastik_ik = {}
    with open(fail2) as fail_ik:
        for rida in fail_ik:
            (ik_vanem, ik_laps) = rida.split()
            sõnastik_ik[ik_vanem] = ik_laps
    uus_sõnastik = {} 
    for vanema_ik, lapse_ik in sõnastik_ik.items(): 
        lapse_ik = sõnastik_ik[vanema_ik]
        lapse_nimi = sõnastik_nimed[lapse_ik]
        for van_ik, laps_ik in sõnastik_ik.items():
            if laps_ik == lapse_ik:
                lapsevanema_ik = van_ik
                uus_sõnastik[laps_ik] = lapsevanema_ik
    return uus_sõnastik 
print(seosta_lapsed_ja_vanemad('nimed.txt', 'lapsed.txt'))