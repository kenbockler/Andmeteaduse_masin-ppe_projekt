aastatulu = float(input("Sisesta aastatulu eurodes: "))
if aastatulu <= 6000:
    maksuvaba_tulu = aastatulu
elif 6000 < aastatulu <= 14400:
    maksuvaba_tulu = 6000
elif 14400 < aastatulu <= 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    maksuvaba_tulu = 0
print("Maksuvaba tulu on", round(maksuvaba_tulu, 2), "eurot")