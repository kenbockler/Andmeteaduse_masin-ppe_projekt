'''
Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid
ja kuvab ekraanile vastavad jalalaba pikkused sentimeetrites �mardatuna t�isarvuks.
Valem jalalaba pikkuse arvutamiseks on: pikkus = 2/3 * (kinganumber - 2).
Faili nende ridade juures, kus arvuks teisendamine miskip�rast eba�nnestub,
tuleb ekraanile kuvada �Vigane sisend� ning j�tkata faili j�rgmise reaga.
'''
fail = open("kinganumbrid.txt","r")
kinganumbrid = fail.readlines()
for kinganumber in kinganumbrid:
    try:
        kinganumber = float(kinganumber)
        kinganumber = 2/3*(kinganumber-2)
        print(round(kinganumber))
    except:
        print("Vigane sisend")
fail.close()
