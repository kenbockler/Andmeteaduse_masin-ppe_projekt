pikkus = int(input("Sisesta elektriliini pikkus meetrites: "))
postide_vahe = int(input("Sisesta maksimaalne k�rvuti olevate postide kaugus meetrites: "))
postide_arv = pikkus // postide_vahe + 1
print("Elektriliini pikkus on", pikkus, "m")
print("K�rvuti asetsevate postide maksimaalne vahemaa on", postide_vahe, "m")
print("Elektriliini ehitamiseks l�heb vaja", postide_arv, "posti")