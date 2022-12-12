kasu = input("Sisestage palun kasutajanimi: ")
while True:
    pw = input ("Sisestage palun parool: ")
    pw2 = input ("Sisestage parool uuesti: ")
    if pw != pw2:
        print("Paroolid ei kattu.")
        continue
    elif len(pw) < 8:
        print ("Parool peab sisaldama vähemalt kaheksat tähemärki.")
        continue
    elif pw.isnumeric() == True or pw.isalpha() == True:
        print("Parool peab koosnema nii tähtedest kui ka numbritest.")
        continue
    else:
        break
umber = "".join(reversed(pw))
f = open("user.txt", "w")
f.write(kasu + ":" + umber)
f.close()
    