aastatulu = float(input("Tere! Palun sisesta teie aastatulu ja vajuta ENTER: "))
if aastatulu <= 6000:
    print("Teie maksuvaba tulu", aastatulu)
else:
    if aastatulu > 6000 and aastatulu <= 14400:
        print("Teie maksuvaba tulu on 6000 eurot aastas.")
    else:
        if aastatulu >= 14400 and aastatulu <= 25200:
            b = round(6000 - (6000 / 10800) * (aastatulu - 14400), 2)
            print("Teil on vaja maksta ",b)
        else:
            print("Teie maksuvaba tulu on 0 eurot aastas.")
