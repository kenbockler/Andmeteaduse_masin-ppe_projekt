aastatulu = int(input("Sisesta aastatulu: "))
if aastatulu < 6000:
    maksuvaba_tulu = aastatulu
elif aastatulu < 14400:
    maksuvaba_tulu = "6000"
elif aastatulu < 25200:
    maksuvaba_tulu = float(6000 - 6000 / 10800 * (aastatulu - 14400))
print("Maksuvaba tulu on:", round(maksuvaba_tulu, 2), "eurot")