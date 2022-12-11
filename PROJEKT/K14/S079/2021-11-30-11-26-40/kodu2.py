def väljasta_liin(eel, järel, sugupuu):
    if järel not in sugupuu.keys():
        return False
    else:
        print(eel)
        for i in range(len(list(sugupuu))):
            s = list(sugupuu.items())[i]
            nimed = s[1]
            if eel in nimed:
                eel2 = list(sugupuu.keys())[i]
                if eel2 == järel:
                    print(järel)
                    return 
                else:
                    väljasta_liin(eel2, järel, sugupuu)
        return True 
