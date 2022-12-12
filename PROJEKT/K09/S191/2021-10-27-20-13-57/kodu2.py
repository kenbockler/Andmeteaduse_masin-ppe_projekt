from random import randint
def minu_shuffle(järj):
    print(järj)
    if len(järj)<2:
        print(järj)
    else:
        kord=randint(10,50)
        while kord>0:
            kord-=1
            pop=järj.pop(randint(0,len(järj)-1))
            järj.insert(randint(0,len(järj)-1),pop)
        print(järj)
