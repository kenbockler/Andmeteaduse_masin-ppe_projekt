liini_pikkus = int(input("Sisestage on liini pikkus meetrites: "))
postidekaugus = int(input("Sisestage postide maksimaalkaugus: "))
postid = 1
postidekaugus2 = 0
while postidekaugus2 < liini_pikkus:
    postidekaugus2 = postidekaugus + postidekaugus2
    postid = postid + 1
print("Poste on kokku " + str(postid))
