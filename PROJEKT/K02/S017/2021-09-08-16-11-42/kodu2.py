import math
print("T�na ehitame sirgjoonelist elektriliini.")
print("Sirgjoonelise elektriliini ehitamisel paigutatakse" "\n" "k�rvutiasetsevad postid v�rdsete kaugustega," "\n" "mis ei �leta etteantud maksimaalkaugust." "\n" "Liin algab ja l�peb postiga.")
pikkus = int(input("Palun sisesta liini pikkus: "))
kaugus = int(input("Sisesta k�rvutiasetsevate postide maksimaalkaugus: "))
jagatis = pikkus / kaugus
x = math.ceil(jagatis) + 1
print("Liini ehitamiseks on minimaalselt vaja", x, "posti")
