n = abs(int(input("Sisesta naturaalarv: ")))
a = 0
i = 1
while i <= n:
    a = a + (i * i)
    i += 1
n_ruut = a
a = 0
i = 1
s = 0
while i <= n:
    a = a + 1
    s = s + a
    i+=1
n_summa = s*s
erinevus = n_summa - n_ruut
print("Naturaalarvu summa ruut on " + str(n_summa) + " Ruutude summa erinevus on " + str(erinevus))