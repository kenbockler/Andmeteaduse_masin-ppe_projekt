#mirjampirn
def auto_hind(n,p):
    if p==0:
        print(n)
    else:
        auto_hind(n-n*20/100,p-1)
        