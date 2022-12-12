import math
n = int(input("Sisestage n väärtus "))
i = 0
j = 0
k = 0
while i != n: 
    j = j + (i + 1)*(i + 1)
    k = k + i + 1
    i = i + 1
k = k * k
print(abs(j - k))
