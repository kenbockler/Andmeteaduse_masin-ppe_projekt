import math
liini_pikkus=float(input("Sisesta liini pikkus meetrites (t�isarvuna): "))
postide_maksimaalkaugus=float(input("Sisesta k�rvuti asuvate postide maksimaalkaugus meetrites (t�isarvuna): "))
postide_arv=float(liini_pikkus/postide_maksimaalkaugus)
print("Liini ehitamiseks on vaja minimaalselt " + str(math.ceil(postide_arv)+1) + " posti.")
