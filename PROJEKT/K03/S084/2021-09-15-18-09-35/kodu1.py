while True:
    try:
        aastatulu = float(input("Sisesta aastatulu: "))
        if aastatulu >= 0:
            break
        print("Arv peab olema positiivne.")
    except:
        print("Midagi läks valesti.")
if aastatulu < 6000:
    maksuvaba = aastatulu
elif 6000 <= aastatulu < 14400:
    maksuvaba = 6000.0
elif 14400 <= aastatulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
else:
    maksuvaba = 0
print(f"Maksuvaba tulu on {round(maksuvaba, 2)} eurot.")