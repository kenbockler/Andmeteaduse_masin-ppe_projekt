teepikkus= float(input("Sisestage teepikkus kilomeetrites: "))
fail = open("taksohinnad.txt", "r", encoding="utf-8")
hinnajärjend = []
nimejärjend = []
for rida in fail:
    uus_järjend= rida.split(",")
    kmhind = uus_järjend[-1]
    sisseistumistasu = uus_järjend[-2]
    taksonimi = uus_järjend[0]
    hind = float(kmhind)*teepikkus+float(sisseistumistasu)
    hinnajärjend.append(hind)
    nimejärjend.append(taksonimi)
väikseim=min(hinnajärjend)
indeks = hinnajärjend.index(väikseim)
odavaim = nimejärjend[indeks]
print ("Kõige odavam on "+odavaim+".")
fail.close()