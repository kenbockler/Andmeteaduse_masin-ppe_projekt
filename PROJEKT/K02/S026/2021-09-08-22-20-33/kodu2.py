a = float(input("Palun sisesta liini piikus (t�isarvuna meetrites): "))
b = float(input("Palun sisesta k�rvutiasetsevate postide maksimaalkaugus (t�isarvuna meetrites): "))
import math
print("Posti vaja liini ehitamiseks:", math.ceil (a / b))
