nimi = str(input("Sisesta kasutajanimi: "))
while True:
    parool_1 = (input("Sisesta parool: "))
    parool_2 = (input("Sisesta parool teist korda: "))
    if parool_1 != parool_2 :
        raise Exception ("Paroolid peavad �htima.")
    elif (len(str(parool_1))) < 8:
        raise Exception ("Parool peab olema v�hemalt 8 t�hem�rki pikk.")
    elif parool_1.isalpha() or parool_1.isdigit():
        raise Exception ("Paroolis peavad olema nii numbrid kui t�hed")
    parool_p��ratud = (parool_2[::-1])
    break
f= open("users.txt", "w")
f.write(nimi + ":" + parool_p��ratud "\n")
f.close()         