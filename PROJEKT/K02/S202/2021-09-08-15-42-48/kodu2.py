from math import *
lp = int(input("Sisestage liini pikkus: "))
pmk = int(input("Sisestage postide maksimum kaugus: "))
mpv = ((lp/pmk) + 1)
print("Vaja läheb " + str(ceil(mpv)) + " post(i).")