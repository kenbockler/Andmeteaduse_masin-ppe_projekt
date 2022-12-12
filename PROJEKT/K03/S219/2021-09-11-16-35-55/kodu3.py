n = int(input("Sisesta naturaalarv n: "))
n1 = n - n + 1
summa = n*(n+1)/2
summaruut = summa * summa
ruutsumma = (n*(n+1)*(2*n+1))/6
vastus = summaruut - ruutsumma
print(vastus)
