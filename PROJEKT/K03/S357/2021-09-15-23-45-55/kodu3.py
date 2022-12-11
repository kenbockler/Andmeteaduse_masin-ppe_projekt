n = int(input("Sisesta naturaalarv "))
list = range(0, (n+1))
y = (sum(list))**2
x = 0
for i in range(0, (n+1)):
    x += i**2
print("Erinevus on ", y-x )