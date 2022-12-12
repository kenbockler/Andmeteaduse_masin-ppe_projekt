def konto():
    while True:
        num = 0
        täht = 0
        parool = input("Sisesta parool: ")
        kontroll = input("Sisesta parool teist korda: ")
        if parool != kontroll:
            print("Paroolid ei kattu.")
        elif len(parool) < 8:
            print("Parool peab olema vähemalt 8 tähemärki pikk.")
        else:
            for i in parool:
                if i.isdigit():
                    num = 1
                elif i.isalpha():
                    täht = 1
            if num + täht == 2:
                return parool
            else:
                print("Parool peab sisaldama nii tähti kui numbreid.")
def kontotoiming(kasutajanimi, parool):
    parool = parool [::-1]
    with open("users.txt", 'w') as f:
        f.write(kasutajanimi+":"+parool+'\n')
kontotoiming(input("Sisesta kasutajanimi: "), konto())