teepikkus = input("Sisesta teepikkus: ")
with open("taksohinnad.txt",encoding="utf-8") as f:
    while True:
        rea_lugemine =  f.read()
        if rea_lugemine == "":
            break
        rea_lugemine.strip()
        eraldi_andmed = rea_lugemine.split(",")
        taksonimi = eraldi_andmed[0]
        sisseistumise_hind = [1]
        km_hind = [2]
        i_sisseistumise_hind = int(sisseistumise_hind)
        i_km_hind = int(km_hind)
        kogu_hind = i_sisseistumise_hind + i_km_hind*teepikkus
