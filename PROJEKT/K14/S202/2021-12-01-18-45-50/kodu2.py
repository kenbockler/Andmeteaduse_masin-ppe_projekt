def väljasta_liin(eellane, järglane, sõnastik):
    global otsitav
    try:
        otsitav.append(eellane)
    except:
        otsitav = []
        otsitav.append(eellane)
    if järglane == otsitav[0]:
        print(järglane)
        return True
    elif järglane in sõnastik:
        isaliin = väljasta_liin(järglane, sõnastik[järglane][0], sõnastik)
        emaliin = väljasta_liin(järglane, sõnastik[järglane][1], sõnastik)
        if (isaliin == True) or (emaliin == True):
            print(järglane)
            return True
        else:
            return False
    elif järglane not in sõnastik:
        return False