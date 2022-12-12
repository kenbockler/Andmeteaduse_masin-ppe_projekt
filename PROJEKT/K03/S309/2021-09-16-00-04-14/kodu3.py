sisend = int(input("Sisestage arv: "))
summaruut = (sum(range(0, sisend + 1)))**2
ruudusumma = 0
for i in range(0, (sisend + 1)):
    ruudusumma += i**2
print(summaruut-ruudusumma)