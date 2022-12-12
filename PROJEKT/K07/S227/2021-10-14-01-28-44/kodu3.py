def sünnikuupäev(isikukood):
    f=list(str(isikukood))
    if f[0] < "5":
        aasta="19"+str(f[1:3])
        päev=str(f[5:7])
        kuu1=str(f[3:5])
        kuu=("").join(kuu1)
        return print("{0}{1}{2}".format(päev,kuu,aasta))
    else:
        aasta="20"+str(f[1:3])
        print(aasta)
sünnikuupäev(34501234215)
väljund=""