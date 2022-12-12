def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    järjend= list(sõne)
    sõnastik={}
    for sümbol in järjend:
        sagedus= järjend.count(sümbol)
        if sümbol not in sõnastik:
            sõnastik[sümbol]= sagedus
    return sõnastik       
def grupeeri(sõne):
    t_häälikud= ('i','ü','u','e','ö','õ','o','ä','a')
    k_häälikud= ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w','x', 'y')
    sõnastik={
            'Täishäälikud': set(),
            'Kaashäälikud': set(),
            'Muud': set()
        }
    sagedus= sümbolite_sagedus(sõne)
    for täht in sagedus:
        if täht.lower() in t_häälikud:
            sõnastik['Täishäälikud'].add(tuple((täht,sagedus[täht])))
        elif täht.lower() in k_häälikud:
            sõnastik['Kaashäälikud'].add(tuple((täht,sagedus[täht])))
        else:
            sõnastik['Muud'].add(tuple((täht,sagedus[täht])))
    return sõnastik
