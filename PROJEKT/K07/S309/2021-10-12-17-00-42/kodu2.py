distance = float(input("Sisesta tee pikkus kilomeetrites: "))
taxifile = open("taksohinnad.txt", "r", encoding="UTF-8")
taxi = ()
taxilist = []
for line in taxifile:
    taxi = tuple(line.strip().split(","))
    taxilist.append([(float(taxi[1]) + float(taxi[2])*float(distance)), taxi[0]])
try:
    taxilist.sort()
    print(f"Kõige odavam on {taxilist[0][1]}")
except Exception as e:
    print(e)
