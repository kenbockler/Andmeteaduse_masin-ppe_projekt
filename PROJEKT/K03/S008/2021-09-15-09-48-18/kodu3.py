arv = int (input ("Sisestage üks naturaalarv: "))
i = 1
j = 1
summa = 0
summa2 = 0
while i <= arv:
    summa = summa + i ** 2
    i +=1
while j <=arv:
    summa2 += j
    j += 1
print (((summa2)**2) - summa)