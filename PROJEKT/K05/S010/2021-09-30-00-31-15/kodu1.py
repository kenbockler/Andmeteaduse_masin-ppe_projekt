kasutajanimi=input("Sisestage oma kasutajanimi: ")
while True:
    parool1=input("Sisestage oma parool: ")
    parool2=input("Sisestage oma parool teist korda: ")
    if parool1!=parool2:
        print("Viga! Sisestatud paroolid ei kattu omavahel!")
        continue
    paroolipikkus=len(parool1)
    if paroolipikkus<8:
        print("Viga! Sisesatud parool on alla 8 t�hem�rgi pikk!")
        print("Sisestage parool, mis on v�hemalt 8 t�hem�rki pikk.")
        continue
    if parool1.isnumeric() or parool1.isalpha():
        print("Viga! Parool peab sisaldama nii t�hti kui ka numbreid!.")
        continue
    break
i=-1
kr�pteering=str()
while i>=-paroolipikkus:
    t�ht=parool1[i]
    kr�pteering+=t�ht
    i-=1
f=open("users.txt", mode="w")
f.write(kasutajanimi+':'+kr�pteering)
f.close()