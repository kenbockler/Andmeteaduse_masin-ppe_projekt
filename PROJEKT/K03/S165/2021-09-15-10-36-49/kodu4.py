LähteFail = "kinganumbrid.txt"
f = open(LähteFail)
while True:
    rida = f.readline()
    if rida == "" or rida == ('\n'): 
        break
    try:
        rida = float(rida)
    except:
        print("Vigane sisend")
        continue
    pikkus = 2/3 * (rida - 2)
    print(round(pikkus))
