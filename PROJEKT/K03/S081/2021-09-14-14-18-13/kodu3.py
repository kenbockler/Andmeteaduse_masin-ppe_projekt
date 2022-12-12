n = int(input('Sisestage naturaalarv: '))
aarv = 1
a2arv = 1
rs=0
sr=0
while aarv <= n:
    rs+= aarv**2
    aarv+=1
while a2arv <= n:
    sr += a2arv
    a2arv +=1
sr = sr**2
er=sr-rs
print(er)