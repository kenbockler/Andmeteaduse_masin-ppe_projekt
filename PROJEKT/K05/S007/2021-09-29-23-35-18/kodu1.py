kasutajanimi = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool teist korda: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if not parool1.isnumeric():
                if not parool1.isalpha():  
                    uus=""
                    for el in parool1:
                        uus=el+uus
                    break
                else:
                    print("Kasuta numbreid.")
                    continue
            else:
                print("Kasuta t�hti.")
                continue
        else:
            print("T�hem�rke on v�hem kui 8.")
            continue
    else:
        print("Paroolid ei kattu.")
        continue
f = open('users.txt', 'w')
f.writelines([kasutajanimi,":",uus])
f.close()
