liini_pikkus = int(input("Palun kirjuta siia liini pikkus (t�isarvuna, meetrites) ja vajuta ENTER: "))
post_kaugus = int(input("Palun kirjuta siia k�rvuti asetsevate postide maksimaalkaugus (t�isarvuna, meetrites) ja vajuta ENTER: "))
min_kogus= int(liini_pikkus / post_kaugus + 2)
if liini_pikkus < post_kaugus:
    print("Liini pikkus ei saa olla l�hem, kui postide kaugus �ksteisest.")
elif liini_pikkus == post_kaugus:
    print("Liini ehitamiseks on vaja minimaalselt 2 posti.")
else:
    print("Liini ehitamiseks on vaja minimaalselt " + str(min_kogus) + " posti")
