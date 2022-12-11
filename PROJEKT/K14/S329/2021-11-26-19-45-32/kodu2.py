def väljasta_liin(enimi, jnimi, sõnastik):
    if jnimi in sõnastik:
        for el in range(2):
            if sõnastik[jnimi][el] == enimi:
                print(enimi)
                print(jnimi)
                return True
            else:
                if väljasta_liin(enimi, sõnastik[jnimi][el], sõnastik) == True:
                    print(jnimi)
                    return True
    return False