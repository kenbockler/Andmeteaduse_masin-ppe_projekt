aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu<6000:
    maksuvaba_tulu= aastatulu
elif aastatulu>25200:
    maksuvaba_tulu=0
elif aastatulu>14400:
    maksuvaba_tulu=6000-6000/10800*(aastatulu-14400)
elif aastatulu>=6000:
    maksuvaba_tulu=6000
print("Maksuvaba tulu on", str(round(maksuvaba_tulu, 2))+ " eurot.")
    