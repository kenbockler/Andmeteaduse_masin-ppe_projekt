import statistics
import matplotlib.pyplot as plt
def silu_andmed(loend, n):
    for i in range(len(loend)):
        kesk_loend = []
        kesk_loend.append(statistics.harmonic_mean(loend[slice(i-1, n+i)]))
    print(kesk_loend)