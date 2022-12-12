km = input("Sisesta tee pikkus kilomeetrites: ")
f = "taksohinnad.txt"
fail = open(f)
järjend = []
nimi = ["Maksitaksi", "Sõps veab", "Waldo takso"]
for rida in fail:
    a = rida.split(",")
    alustustasu = a[1]
    km_hind = a[2]
    b = km_hind.strip()
    sõidu_hind = str(float(alustustasu) + float(km)*float(b))
    järjend.append(sõidu_hind)
indeks = 0
miinimum = järjend[0]
for i in range(len(järjend)):
    if järjend[i] < miinimum:
        miinimum = järjend[i]
        indeks = i
takso = nimi[indeks]
print("Kõige odavam on " + takso)
fail.close()
