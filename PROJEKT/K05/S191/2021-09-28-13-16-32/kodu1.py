k_nimi=input("Sisestage kasutajanimi: ")
while True:
    pass1=input("Sisestage parool: ")
    pass2=input("Sisestage uuesti: ")
    if pass1 !=pass2:
        print("Paroolid ei ühti \n")
    elif len(pass1)<8:
        print("Parool liiga lühike\n")
    elif any(i.isdigit() for i in pass1)==False:
        print("Parool peab sisaldama numbreid\n")
    else:
        break
krypt=pass1 [::-1]
f=open("users.txt","a")
f.write(k_nimi+":"+krypt+"\n")
f.close()