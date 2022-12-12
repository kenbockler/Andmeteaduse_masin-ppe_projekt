Pikkus = int(input("Palun sisestage liini pikkus meetrites (täisarv): "))
Kaugus = int(input("Palun sisestage maksimaalne vahemaa postide vahel meetrites (täisarv): "))
Postide_arv = (Pikkus // Kaugus)
if Kaugus >= (51) :
    print("Kahe posti vaheline kaugus ei saa olla rohkem kui 50 meetrit.")
if Pikkus <= Kaugus :
            print("Liini pikkus ei saa olla pikem kui maksimaalne vahe postidel.")
else:
    print(Postide_arv)