from random import randint
import string
def suurväike(line):
    new_line = ''
    line = line.swapcase()
    rand_punct = string.punctuation[randint(0, 31)]
    for i in line:
        if i in string.punctuation:
            i = rand_punct
        new_line += i
    return new_line