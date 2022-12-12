from math import*
liini_pikkus= int(input("Sisestage liini pikkus (täisarvuna meetrites): "))
postidevaheline_kaugus_maks=int(input("Kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
postide_arv=ceil((liini_pikkus/postidevaheline_kaugus_maks)+1)
print(postide_arv)
