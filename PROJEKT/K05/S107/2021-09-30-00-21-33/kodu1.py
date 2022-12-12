f = open("users.txt", 'w')
kasutajanimi = input("Palun sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    if not parool1 == parool2:
        print("Parool ei vasta nõuetele")
        continue
    elif not (len(parool1) >=8):
        print("Parool ei vasta nõuetele")
        continue
    if not any(x.isdigit() for x in parool1) > 0:
        print("Parool ei vasta nõuetele")
        continue
    tagurpidi = parool1[::-1]
    f.write(kasutajanimi + ":" + tagurpidi)
    break
f.close()