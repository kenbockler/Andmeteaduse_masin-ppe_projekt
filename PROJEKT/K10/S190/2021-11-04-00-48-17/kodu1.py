sõne_üks = input("Sisesta mingi lause: ")
def erinevad_sümbolid(sõne_üks):
    hulk_üks = set(sõne_üks)
    return hulk_üks
sõne_kaks = input("Sisesta mingi lause: ")
sõnastik_kaks = dict()
def sümbolite_sagedus(sõne_kaks):
    hulk_kaks = set(sõne_kaks)
    for täht in hulk_kaks:
        arv = sõne_kaks.count(täht)
        sõnastik_kaks[täht] = arv
    return sõnastik_kaks
sõne_kolm = input("Sisesta mingi lause: ")
sõnastik_kolm = dict()
täishäälikud = []
kaashäälikud = []
muu = []
def grupeeri(sõne_kolm):
    hulk_kolm = set(sõne_kolm)
    for täht in hulk_kolm:
        arv = sõne_kolm.count(täht)
        sõnastik_kolm[täht] = arv
        for võti,väärtus in sõnastik_kolm.items():
            if võti.lower() in {"a","e","i","o","u","õ","ä","ö","ü"}:
                täishäälikud.append((võti,väärtus))
            elif võti.lower() in {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v", "w","x","y","z"}:
                kaashäälikud.append((võti,väärtus))
            else:
                muu.append((võti,väärtus))
    täish_hulk = set(täishäälikud)
    kaash_hulk = set(kaashäälikud)
    muu_hulk = set(muu)
    häälikute_dict = dict()
    häälikute_dict["Täishäälikud"] = täish_hulk
    häälikute_dict["Kaashäälikud"] = kaash_hulk
    häälikute_dict["Muud"] = muu_hulk
    return häälikute_dict