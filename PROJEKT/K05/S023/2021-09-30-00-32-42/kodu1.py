kasutajanimi = input("Sisestage kasutajanimi: ")
parool = input("Sisestage parool: ")
parool2 = input("Sisestage parool teist korda: ")
while parool != parool2 or len(parool) < 8 or parool.isalpha() != parool2.isnumeric():
    if parool != parool2:
        print("Parool ei kattu oma kordusega! Sisestage uus parool!")
    if len(parool) < 8:
        print("Parool on l�hem kui v�hemalt 8 t�hem�rki!")
    if parool.isalpha() != parool2.isnumeric():
        print("Parool ei sisalda numbreid ja t�hti!")
    parool = input("Sisestage uus parool")
    parool2 = input("Sisestage uus parool teist korda")
uusparool = parool[::-1]
fail = open("users.txt",'w+')
fail.write(kasutajanimi+":"+uusparool)
fail.close()