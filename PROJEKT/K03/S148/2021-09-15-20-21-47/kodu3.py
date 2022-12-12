n = int(input("Sisesta naturaalarvude arv: "))
i = 1
a = 0
while i <= n:
    a += i**2
    i += 1
j = 1
b = 0
while j <= n:
    b += j
    j += 1
c = b**2
print(c - a)