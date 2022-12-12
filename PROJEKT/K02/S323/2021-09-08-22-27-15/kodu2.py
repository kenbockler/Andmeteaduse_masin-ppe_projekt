import math
pikkus = float(input("Sisestage elektriliini pikkus: "))
vahe = float(input("Sisestage postide maksimaalne vahe: "))
if pikkus == round(pikkus) and vahe == round(vahe):
    tulemus = math.ceil(pikkus / vahe) + 1
    print("Minimaalselt läheb elektriliini ehitamiseks vaja", str(tulemus), "posti.")