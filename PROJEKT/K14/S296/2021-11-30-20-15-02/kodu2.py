def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == eellane:
        print(eellane)
        return True
    if järglane in sõnastik:
        for i in sõnastik:
            if i == järglane:
                for j in sõnastik[i]:
                    a=väljasta_liin(eellane,j,sõnastik)
                    if a == True:
                        print(järglane)
                        return True
                return a
    elif järglane not in sõnastik:
        a=False
        return a
