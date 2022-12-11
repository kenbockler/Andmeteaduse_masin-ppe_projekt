from random import sample
def bingo():
     numbers = sample(range(1, 11),3) + sample(range(11, 21),2)
     subn = numbers[:3]
     while True:
        if 1 in subn and 2 in subn and 3 in subn:
             numbers = sample(range(1, 11),3) + sample(range(11, 21),2)
        else:
             break
     return numbers
