nimi=input("Sisesta kasutajanimi: ")
tagurpidi=""
while True:
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if parool1!=parool2:
        print("Paroolid ei kattu, proovi uuesti!","\n")
        continue
    if len(parool1)<8:
        print("Parool on liiga lühike, proovi uuesti!", "\n")
        continue
    tähed=0
    numbrid=0
    for sümbol in parool1:
        if sümbol.isdigit():
            numbrid+=1
        if sümbol.isalpha():
            tähed+=1.
    if tähed<1 or numbrid <1:
        print("Parool peab sisaldama vähemalt ühte numbrit ja ühte tähte, proovi uuesti!","\n")
        continue
    break
for sümbol in parool1[::-1]:
    tagurpidi+=sümbol
f=open("users.txt","w")
f.write(nimi+":"+tagurpidi)
f.close()
