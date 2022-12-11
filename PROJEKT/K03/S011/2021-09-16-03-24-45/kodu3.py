n = int(input("siseta naturaalarv: "))
x = ((1+n)*n/2)**2
y = 0
while n > 0 :
    n = n
    y = y+(n)**2
    n=n-1
print(x)
print(y)
print(x-y)