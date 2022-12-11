liini_pikkus = int(input("Sisestage liini pikkus (täisarvuna meetrites): "))
maksimaalkaugus = int(input("Sisestage Kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
postid = 1
while liini_pikkus > maksimaalkaugus:
    postid+=1
    liini_pikkus-=maksimaalkaugus
if liini_pikkus > 0:
    postid+=1
print("Liini ehitamiseks on minimaalselt vaja", postid, "posti.")