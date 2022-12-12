kasutajanimi = input("Sisestage kasutajanimi: ")
while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    if parool1 == parool2:
        if len(parool2) >= 8:
            if any(char.isdigit() for char in parool2) == True:
                if any(char.isalpha() for char in parool2) == True:
                    break
    else:
        print("Teie paroolid ei ühti. Sisestage paroolid uuesti.")
        