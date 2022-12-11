from statistics import harmonic_mean
y = open('aktsiad.txt', encoding ='UTF-8')
b = []
x = []
c = 1
f = 0
d = 0
def silu_andmed(a, b):
   while True:
        rida = y.readline().strip()
        if rida =='':
            break
        uus = rida.split(',')
        b +=[float(uus[1])]
   while f < len(b):
        x.append(harmonic_mean(b[d:c]))
        c +=1
        if 3<c:
            d +=1
        f +=1
print(b)
b = x
print(b)
    