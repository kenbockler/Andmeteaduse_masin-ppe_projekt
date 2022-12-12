from statistics import harmonic_mean
import matplotlib.pyplot as plt
kuupäevad = []
kuupäevade = len(kuupäevad)
hinnad = []
hindade = len(hinnad)
fail = input("Sisesta algandmete fail:")
failist_lugemine = open(fail)
for rida in failist_lugemine:
    read = rida.strip().split(", ")
    kuupäev = read[0]
    hind = read[1]
    kuupäevad.append(kuupäev)
    hinnad.append(hind)
def silu_andmed(hinnad, n):
    keskmistatud_andmed = [harmonic_mean([hinnad[0]]), harmonic_mean(hinnad[0:n-1]), harmonic_mean(hinnad[0:n]), harmonic_mean(hinnad[n-2:n+1]), harmonic_mean(hinnad[n-1:n+2])]
    return keskmistatud_andmed