def moos (x, y, z):
    karpideArv=0
    while True:
        if z>=5 and x>0:
            z-=5
            x-=1
            karpideArv+=1
        elif z==0:
            return karpideArv
            break
        elif y>=z:
            karpideArv+=z
            return karpideArv
            break
        else:
            return -1
            break
suured=int(input("Sisesta suurte karpide arv: "))
väiksed=int(input("Sisesta väikeste karpide arv: "))
kogus=int(input("Sisesta keedetava moosi kogus kilogrammides: "))
moos(suured, väiksed, kogus)