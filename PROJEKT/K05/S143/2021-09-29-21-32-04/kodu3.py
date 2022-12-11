a = 0
def moos(s,v,k):
    return(int(k/5) if (s!=0 and k%5==0 and v<k and v!=0 and k/5<=s) else (-1 if k>(s*5+v*1) else (s+v if k==(s*5+v*1) else ((lambda x: lambda y,z,w,q: x(x,y,z,w,q))(lambda s,L,S,W,I: I+W if (W<5 and S>=W) else (-1 if (W<5 and W>S) else (-1 if (W > 1 and S == 0) else (s(s,L-1,S,W-5,I+1) if (L>0 and W>=5) else (s(s,L,S-1,W-1,I+1))))))(s,v,k,a)))))
print(moos(1,3,4))
