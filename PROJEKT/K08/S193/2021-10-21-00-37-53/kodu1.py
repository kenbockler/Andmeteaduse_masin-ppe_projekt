from random import sample
def bingo():
    esimene_vahemik = sample(range(1, 11), 3)
    teine_vahemik = sample(range(11, 21), 2)
    while 1 in esimene_vahemik and 2 in esimene_vahemik and 3 in esimene_vahemik:
        esimene_vahemik = sample(range(1, 11), 3)
    return esimene_vahemik + teine_vahemik
