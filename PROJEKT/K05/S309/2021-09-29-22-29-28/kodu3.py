def moos(bigcount, smallcount, jamamount):
    if((bigcount*5 + smallcount) < jamamount):
        return -1
    big = jamamount // 5
    if(big > bigcount):
        big = bigcount
    small = (jamamount - big*5)
    if(smallcount >= small):
        return (big + small)
    else:
        return -1