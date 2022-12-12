while True:
    kasutajanimi = input("Sisesta kasutajanimi: ")
    esimene_parool = input("Sisesta parool esimest korda: ")
    teine_parool = input("Sisesta parool teist korda: ")
    if esimene_parool != teine_parool:
        print("Paroolid pole samad.\n")
        continue
    count = len(esimene_parool)
    if count < 8:
        print("Parool liiga lühike.\n")
        continue
    onTäht = False
    onNumber = False
    for char in esimene_parool:
        if char.isalpha():
            onTäht = True
        if char.isdigit():
            onNumber = True
    if onTäht == False or onNumber == False:
        print("Pole ühte tähte või numbrit.\n")
        continue
    break
reverse = "".join(reversed(esimene_parool))
formatted = kasutajanimi + ":" + reverse
with open("users.txt", "w") as file:
    file.write(formatted)
    print("Success.")
