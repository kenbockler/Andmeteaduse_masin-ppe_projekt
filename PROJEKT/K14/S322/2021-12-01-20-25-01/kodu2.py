def väljasta_liin(eellane, järglane, sugupuu):
    if eellane == järglane:
        print(eellane)
        return True
    else:
        järgmine = None
        for key in sugupuu.keys():
            if (sugupuu[key][0] == eellane) or (sugupuu[key][1] == eellane):
                järgmine = key
                break
        if järgmine == None:
            return False
        elif väljasta_liin(järgmine, järglane, sugupuu):
            print(eellane)
            return True
        else:
            return False
