from random import sample
def bingo():
    esimene_arv = sample(range(1,11), 3)
    if sum(esimene_arv) == 6:
        esimene_arv = sample(range(1,11), 3)
        return esimene_arv
    teine_arv = sample(range(11,21), 2)
    väljund = esimene_arv + teine_arv
    return väljund
    