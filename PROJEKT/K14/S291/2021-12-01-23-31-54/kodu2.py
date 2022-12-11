def väljasta_liin(eellase_nimi, järglase_nimi, sugupuu_sõnastik):
    for võti in sugupuu_sõnastik:
        if sugupuu_sõnastik[võti][0] == eellase_nimi or sugupuu_sõnastik[võti][1] == eellase_nimi:
            print(eellase_nimi)
            if võti == järglase_nimi:
                print(järglase_nimi)
                break
            else:
                väljasta_liin(võti, järglase_nimi, sugupuu_sõnastik)
    return True