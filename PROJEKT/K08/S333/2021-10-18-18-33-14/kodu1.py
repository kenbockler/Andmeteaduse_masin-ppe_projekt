from random import sample
def bingo():
    esimene= list(range(1,11))
    teine= list(range(11,21))
    bingo1_3=[]
    bingo4_5=[]
    i=0
    n=0
    while i <3:
        arv=sample(esimene,1)
        arv= arv[0]
        if arv in range(1,4): 
            if n<1:
                n+=1
                pass
            else:
                continue
        elif arv in bingo1_3:
            continue
        i+=1 
        bingo1_3= bingo1_3+ [arv]
    i=0
    while i <2:
        arv=sample(teine,1)
        arv= arv[0]
        if arv in bingo4_5:
            continue
        i+=1
        bingo4_5= bingo4_5+ [arv]    
    return bingo1_3 + bingo4_5
