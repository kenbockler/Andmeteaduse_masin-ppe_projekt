aastatulu = float(input("Aastatulu: "))
if aastatulu <= 6000:
    maksuvaba_tulu = aastatulu
else:
    if aastatulu <= 14400:
        maksuvaba_tulu = 6000
    elif aastatulu <= 25200:
        maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
    else:
        maksuvaba_tulu = 0
print(round(maksuvaba_tulu,2))