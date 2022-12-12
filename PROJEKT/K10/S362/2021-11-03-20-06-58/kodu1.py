def erinevad_sümbolid(sõne):
    sõnede_hulk=set(sõne)
    return sõnede_hulk
sõne="hulk ei sisalda kunagi korduvaid elemente"
def sümbolite_sagedus(sõne):
    sõnastik={}
    sone_järjend=list(sõne)
    for i in range(len(sone_järjend)):
        lugeja=1
        for j in range(len(sone_järjend)):
            if sone_järjend[i]==sone_järjend[j] and i!=j:
                lugeja=lugeja+1
        sõnastik[sone_järjend[i]] =  lugeja
    return sõnastik
sõne="Hei hopsti, väikevend!"
def grupeeri(sõne):
    täielik_sõnastik={}
    täishäälikute_hulk=set()
    kaashäälikute_hulk=set()
    muud_hulk=set()
    sõnastik=sümbolite_sagedus(sõne)
    täishäälikud="aeiouõäöü"
    kaashäälikud="bcdfghjklmnpqrsšzžtvwxy"
    täishäälikud_järjend=list(täishäälikud)
    kaashäälikud_järjend=list(kaashäälikud)
    for i in range(3):
        for el in sõnastik:
            elemendi_järjend=[el, sõnastik[el]]
            elemendi_ennik=tuple(elemendi_järjend)
            if (el.lower()) in täishäälikud_järjend: 
                täishäälikute_hulk.add(elemendi_ennik)
            elif (el.lower()) in kaashäälikud_järjend:
               kaashäälikute_hulk.add(elemendi_ennik)
            else:
                muud_hulk.add(elemendi_ennik)
        liba_järjend=["Täishäälikud", "Kaashäälikud", "Muud"]
        hulkade_järjend=[täishäälikute_hulk, kaashäälikute_hulk, muud_hulk]
        täielik_sõnastik[liba_järjend[i]]=hulkade_järjend[i]
    return täielik_sõnastik
sõne="sõida tasa üle silla" 
print(grupeeri(sõne)) 
