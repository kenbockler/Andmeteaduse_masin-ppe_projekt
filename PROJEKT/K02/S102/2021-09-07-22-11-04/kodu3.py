m=input('Sisesta eesnimi: ').lower()
n=input('Sisesta perenimi: ').lower()
m=m.replace('ö'or'õ','o')
m=m.replace('ü','u')
m=m.replace('ä','a')
n=n.replace('õ'or'ö','o')
n=n.replace('ü','u')
n=n.replace('ä','a')
m=m.replace('Ö'or'Õ','o')
m=m.replace('Ü','u')
m=m.replace('Ä','a')
n=n.replace('Õ'or'Ö','o')
n=n.replace('Ü','u')
n=n.replace('Ä','a')
print(m+"."+n)