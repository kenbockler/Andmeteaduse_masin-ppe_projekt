kasutajanimi=input("Sisesta kasutajanimi: ")
t�hti=0
numbreid=0
while True:
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if len(parool1)<8:
        print("Parool on l�hikesev�itu. Vali parool, mis on v�hemalt 8 t�hem�rki pikk.")
        continue
    for i in parool1:
        if i.isalpha():
            t�hti+=1
        elif i.isdigit():
            numbreid+=1
    if t�hti<1 or numbreid<1:
        print("Paroolis peab olema v�hemalt �ks t�ht ja v�hemalt 1 number. Proovi uuesti!")
    elif parool1!=parool2:
        print("Paroolid ei kattu. Proovi uuesti!")
    elif parool1==parool2:
        break
with open("users.txt", "w") as sihtfail:
    sihtfail.write(kasutajanimi+(parool1[::-1]))
    