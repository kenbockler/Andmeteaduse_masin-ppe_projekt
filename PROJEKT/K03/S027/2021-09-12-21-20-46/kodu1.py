tulu = float(input('Sisestage aasta tulu: '))
if tulu < 6000:
    maksuvaba = tulu
elif tulu < 14400:
    maksuvaba = 6000
elif tulu < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (tulu - 14400)
elif tulu >= 25200:
    maksuvaba = 0
maksuvaba_r = round(maksuvaba, 2)
print('maksuvaba tulu on ' + str(maksuvaba_r) + ' eurot.')