nimi = input("Sisestage kasutajanimi: ")
while True:
    parool = input('Sisestage parool: ')
    parool2 = input('Sisestage parool teist korda: ')
    if parool != parool2:
        print('Esimene parool ei kattu teise parooliga!\n')
    elif len(parool) < 8:
        print("Valitud parool on liiga lühike!\n")
    kontroll1 = 0
    kontroll2 = 0
    for i in parool:
        numbrid = ['0','1','2','3','4','5','6','7','8','9']
        if i in numbrid:
            kontroll1 = 1
        else:
            kontroll2 = 1
    if kontroll1 == 0 or kontroll2 == 0:
        print('Kasutage paroolis nii tähti kui numbreid!')
    else:
        break
parool = parool[::-1]
f = open('users.txt', 'w')
f.write(nimi + ':' + parool)
f.close()
