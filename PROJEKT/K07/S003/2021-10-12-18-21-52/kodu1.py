def poisse_ja_t�drukuid(j�rjend):
    n = 0
    m = 0
    if len(j�rjend) != 0:
        for el in j�rjend:
            if  el[-1] == 'P':
                n +=1
            else:
                m +=1
        return (n,m)
    else:
        return (n,m)
