kasutajanimi = input("Mis kasutaja nimeks soovite? ")
def flip(parool2):
    return parool2[::-1]
while True:
    parool = input("sisestage võimalik parool ")
    parool2 = input("palun korrake parooli ")
    if parool != parool2:
        print("sisestage sama parool")
        continue
    elif len(parool2) < 8:
        print("parool peab olema vähemalt 8 tähemärki")
        continue
    elif parool2.isalpha() or parool2.isdigit():
        print("parool peab sisaldama numbreid ja tähti")
        continue
    break
f = open('users.txt', "a")
f.write("\n" + kasutajanimi + ":" + flip(parool2))
f.close()
