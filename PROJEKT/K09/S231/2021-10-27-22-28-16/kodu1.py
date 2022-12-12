file = open("aktsiad.txt")
b = []
while True:
    rida = file.readline()
    if rida == "":
        break
    a = (rida.split(",")[-1].strip())
    a = float(a)
    b.append(a)
from statistics import harmonic_mean
harmonic_mean([a])
print(a)
