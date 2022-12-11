pikkus=int(input("Palun sisestage liini pikkus täisarvuna meetrites: "))
laius=int(input("Palun sisestage kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites: "))
#kuna min vahe saab täisarvude vahel olla 1, siis
postidearv=round(pikkus/laius)+1

if pikkus<laius:
    postidearv=2

print("Poste läheb vaja "+str(postidearv))