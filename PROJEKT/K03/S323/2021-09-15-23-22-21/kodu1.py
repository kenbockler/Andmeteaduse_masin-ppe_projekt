at = float(input("Sisestage aastatulu: "))
mv = 0
if at <= 6000:
    mv = at
elif at <= 14400:
    mv = 6000
elif at <= 25200:
    mv = 6000 - 6000 / 10800 * (at - 14400)
elif at > 25200:
    mv = 0
print("Maksuvaba tulu on "+ str(round(mv, 2)))