'''Kirjuta programm, mis realiseerib ühe veebilehe registreerimisvormi algoritmi.'''
'''******************************'''
def on_numbreid(sone):
    numbreid = 0
    for i in range(9):
        if str(i) in sone:
            numbreid += 1
    if numbreid != 0:
        return True
    return False
'''******************************'''
def tagurpidi(sone):
    pooratud = ""
    for i in reversed(range(len(sone))):
        pooratud += sone[i]
    return pooratud
'''******************************'''
print("*"*100)
print("Tere tulemast meie veebilehe registreerimisvormi. Täida vorm.")
print("*"*100)
kasutajanimi = input("Kasutajanimi: ").strip()
while True:
    salasona_ = input("Salasõna: ").strip()
    salasona = input("Korda salasõna: ").strip()
    if salasona != salasona_:
        print("Salasõnad ei ole võrdsed. Sisesta uuesti.")
    if len(salasona) < 8:
        print("Salasõna peab olema vähemalt 8 tähemärki pikk. Sisesta uuesti.")
    elif on_numbreid(salasona) == False or salasona.isdigit():
        print("Salasõna peab koosnema nii tähtedest kui ka numbritest.")
    else:
        break
f = open("users.txt", "w")
f.write(kasutajanimi+":"+tagurpidi(salasona))
f.close()
print("*"*100)
print("Täname. Teie andmed on salvestatud.")
print("*"*100)