tulu=float(input("Sisesta enda aastatulu: "))
if tulu<6000:
    print("Maksuvaba tulu on "+str(round(tulu, 2))+" eurot. Soovitan �hendust v�tta kohaliku omavalitsuse sotsiaalt��tajaga, kes saab n�u ja j�uga abistada!")
elif 6000<=tulu<14400:
    print("Maksuvaba tulu on 6000,00 eurot. Ehk soovid teha t��ampse, et pisut lisa teenida? Loe selle kohta T��tukassa kodulehelt!")
elif 14400<=tulu<25200:
    print("Maksuvaba tulu on "+str(round(6000-6000/10800*(tulu-14400),2))+" eurot. J�tka samas vaimus!")
else:
    print("Maksuvaba tulu on 0 eurot. Palju �nne suure aastase sissetuleku puhul! Sinu makstud maksud aitavad kaasa tasuta koolihariduse k�ttesaadavusele:))")
          