def poisse_ja_t�drukuid(j�rjend):
    poisid= 0
    t�drukud= 0
    for rida in j�rjend:
        uus_j�rjend = rida.split(" ")
        for el in uus_j�rjend:
            if el == "P":
                poisid +=1 
            elif el == "T":
                t�drukud +=1
    return(poisid, t�drukud)
print(poisse_ja_t�drukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'J�ri P', 'Veronika T']))
