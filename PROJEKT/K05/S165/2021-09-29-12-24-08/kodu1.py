nimi = input("Palun sisestage oma kasutajanimi: ")
def arvjatäht(string):
    arv = False
    täht = False
    for sümbol in string:
        try:
            int(sümbol)
        except:
            sümbol = sümbol.lower()
            if sümbol.islower() == True:
                täht = True
        else:    
            arv = True
        finally:
            if täht == True and arv == True:
                return True
                break
while True:
    parool = input("Palun sisestage oma kasutaja parool: ")
    parool2 = input("Palun sisestage oma kasutaja parool: ")
    if parool != parool2:
        print("Teie paroolid ei olnud samasugused, proovige uuesti!")
        continue
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemärki pikk!")
        continue
    elif arvjatäht(parool) != True:
        continue
    break
uus_parool = []
parool = list(parool)
for i in range(len(parool)):
    uus_parool.insert(len(parool) -1 , parool[(i * -1) - 1])   
uus_parool = "".join(uus_parool)
f = open("users.txt", "w")
f.write(nimi + ":" + uus_parool)
f.close()
