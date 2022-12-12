i = 1
x = 0
ruut = 0
summ = 0
a = input("Sisestage naturaalarv: ")
while(True):    
    if a.isdigit():
        a = int(a)
        break
    else:
        a = input("Sisestage naturaalarv: ")
while i <= a:
    s = i ** 2
    i += 1
    ruut += s
while x <= a:
    summ += x
    x += 1
summ **= 2
print(summ - ruut)