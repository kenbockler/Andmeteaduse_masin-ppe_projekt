def seosta_lapsed_ja_vanemad(lapsed,nime_fail):
    isikukoodid=open(lapsed, encoding="UTF-8")
    nimed=open(nime_fail, encoding="UTF-8")
    vastus={}
    isikukoodide_järjend=[]
    nimede_järjend=[]
    for rida in isikukoodid:
        osad=rida.split(" ")
        for osa in osad:
            isikukoodide_järjend.append(osa.strip("\n"))
    for rida in nimed:
        osad=rida.split(" ")
        for osa in osad:
            nimede_järjend.append(osa.strip("\n"))
    lapse_indeks=1
    laps_ja_lapsevanem=[]
    while lapse_indeks<len(isikukoodide_järjend):
        andmed=[]
        for element in nimede_järjend:
            if element==isikukoodide_järjend[lapse_indeks]:
                elemendi_indeks=nimede_järjend.index(element)
                lapse_nimi=nimede_järjend[elemendi_indeks+1]+ " " + nimede_järjend[elemendi_indeks+2]
                andmed.append(lapse_nimi)
                for elemendikene in nimede_järjend:
                    if elemendikene==isikukoodide_järjend[(lapse_indeks-1)]:
                        elemendikese_indeks=nimede_järjend.index(elemendikene)
                        lapsevanema_nimi=nimede_järjend[elemendikese_indeks+1]+ " " + nimede_järjend[elemendikese_indeks+2]
                        andmed.append(lapsevanema_nimi)
        lapse_indeks+=2
        laps_ja_lapsevanem.append(andmed)
    for laps in laps_ja_lapsevanem:
        vastus[laps[0]]=set()
    for laps in laps_ja_lapsevanem:
        vastus[laps[0]].add(laps[1])
    return vastus
                