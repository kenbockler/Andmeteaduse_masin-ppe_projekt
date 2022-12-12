aastatulu=int(input("Sisestage aastatulu: "))
if aastatulu <= 6000:
    print("Maksuvaba tulu on " + str(aastatulu) + " eurot")
elif aastatulu > 6000 and aastatulu< 14400:
    print("Maksuvaba tulu on 6000 eurot")
elif aastatulu > 14400 and aastatulu<25200:
    maksuvaba_tulu=6000 - 6000 / 10800 * (int(aastatulu) - 14400)
    maksuvaba_tulu=round(maksuvaba_tulu, 2)
    print("Maksuvaba tulu on " + str(maksuvaba_tulu) + " eurot")
else:
    print("Maksuvaba tulu on 0 eurot")
    