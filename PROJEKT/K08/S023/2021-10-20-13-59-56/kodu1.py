from random import sample
def bingo():
    while True:
        a =sample(range(1,11),3)
        b = sample(range(11,21),2)
        j�rjend = a + b
        korras = 0
        if 1 in j�rjend[0:3] and 2 in j�rjend[0:3] and 3 in j�rjend[0:3]:
            print("Genereeritakse uus j�rjend")
            j�rjend = []
        else:
            return j�rjend
            break
print(bingo())