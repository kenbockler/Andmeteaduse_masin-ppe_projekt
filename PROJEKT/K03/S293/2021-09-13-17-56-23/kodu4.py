f = open("kinganumbrid.txt", "r", encoding="UTF-8")
while True:
    kiriandmed= f.readline()
    if kiriandmed == "":
        break
    try:
        arvandmed=float(kiriandmed)
        jala_pikkus=(round(2/3 *(arvandmed -2)))
        print(jala_pikkus)
    except:
        print("Vigane sisend")
f.close()