from random import sample
def bingo():
    while True:
        järjend2 = []
        n2 = sample(range(11,21),2)
        järjend2 = järjend2 + n2
        järjend1 = []
        n1 = sample(range(1,11),3)
        järjend1 = järjend1 + n1
        if sum(järjend1) !=6:
            järjend = järjend1 + järjend2
            return järjend
print(bingo())
    