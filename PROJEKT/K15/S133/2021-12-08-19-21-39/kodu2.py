def järjesta_punktid(p):
    a=[]
    m=(1000,10000)
    if p!=[] and len(p)!=1:
        for i in range(len(p)):
            for j in range(i,len(p)):
                if p[i][1]>p[j][1]:
                    p[i],p[j]=p[j],p[i]
                elif p[i][1]==p[j][1] and p[i][0]>p[j][0]:
                    p[i],p[j]=p[j],p[i]