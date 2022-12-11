aastatulu = float(input("Sisestage oma aastatulu: "))
if aastatulu < 0:
    print("Palun sisesta positiivne arv")
elif aastatulu < 6000:
    print ("Sinu aastane maksuvaba tulu on: " + str((aastatulu)) + " eurot.")
elif aastatulu >= 6000 and aastatulu <= 14400:
    print ("Sinu aastane maksuvaba tulu on: " + "6000" + " eurot.")
elif aastatulu > 14400 and aastatulu < 25200:
    maksuvaba = 6000-6000/10800*(aastatulu - 14400)
    ümardatud = round(maksuvaba, 2)
    print ("Sinu aastane maksuvaba tulu on: " + str(ümardatud) + " eurot.")
else:
    print ("Sinu aastane maksuvaba tulu on: " + "0" + " eurot.")