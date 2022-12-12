kasutajanimi = input("Sisestage kasutajanimi: ")
error1 = 0
error2 = 0
error3 = 0
while True:
    if error1 == 1:
        print("Sisestatud paroolid erinevad!")
    elif error2 == 1:
        print("Parool peab sisaldama vähemalt 8 tähemärki!")
    elif error3 == 1:
        print("Parool peab sisaldama nii tähti kui numbreid!")
    parool = input("Sisestage parool: ")
    pparool = input("Sisestage uuesti parool: ")
    if parool == pparool:
        error1 = 0
        if len(parool) >= 8:
            error2 = 0
            if (parool.isalpha() == False) and (parool.isnumeric() == False):
                error3 = 0
                break
            else:
                error3 = 1
        else:
            error2 = 1
    else:
        error1 = 1
enc = parool[len(parool):: -1]
f = open("users.txt", "w")
f.write(kasutajanimi + ":" + enc)
f.close()