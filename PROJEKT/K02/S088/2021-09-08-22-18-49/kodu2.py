from math import ceil, floor
liin = round(float(input("Mis on liini pikkus meetrites?: ")))
vahe = round(float(input("Mis on elektripostide vahe?: ")))
if liin < 0:
    liin = liin * -1
else:
    liin = liin
if vahe < 0:
    vahe = vahe * -1
else:
    vahe = vahe
postid = liin / vahe + 1
postid = ceil(postid)
print("Vaja on vahemalt ", postid, " posti.")
    