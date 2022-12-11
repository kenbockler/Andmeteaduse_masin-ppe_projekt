n=int(input("Sisesta naturaalarv: "))
i=1
x=0
y=0
while i<=n:
    x=x+i**2
    y=y+i
    i=i+1
else:
    summaruut=y**2
print(summaruut - x)