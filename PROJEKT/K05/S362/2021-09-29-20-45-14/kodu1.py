from math import *
def paroolikontroll(parool1):
    tähti=0
    numbreid=0
    sõne_pikkus=len(parool1)
    if sõne_pikkus>=8:
        u=0
        for letters in parool1:
            if letters.isdigit():
                numbreid=numbreid+1
            elif letters.isalpha():
                    tähti=tähti+1
        if numbreid>0 and tähti>0:
            u=0
        elif numbreid<=0 or tähti<=0:
            print("Tekst peab sisaldama nii tähti kui ka numbreid.")
            u=1
    else:
        print("Parool on liiga lühike.")
        u=1
    return u
kasutajanimi=input("Sisestage oma kasutaja nimi: ")
while True:
    parool1=input("Sisestage oma parool: ")
    parool2=input("Sisestage oma parool veel kord: ")
    if parool1==parool2:
        v=paroolikontroll(parool1)
        if v==0:
            tulemus=''
            for täht in range(len(parool1)-1,-1,-1):
                tulemus=tulemus+parool1[täht]
            parool=parool1
            f=open("users.txt", "w", encoding="UTF-8")
            f.write(kasutajanimi+":"+tulemus+"\n")
            f.close()
            break
        else:
            print("Proovi uuesti.")
    else:
        print("Vale parool. Proovi uuesti.")