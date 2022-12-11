def sünnikuupäev(isikukood):
    isikukood= list(str(isikukood))
    päev= isikukood[5:7]
    päev= int(päev[0]+ päev[1])
    kuu= isikukood[3:5]
    if kuu[0]=='0':
        kuu= int(kuu[1])
    elif kuu[0]=='1':
        kuu= int(kuu[0]+ kuu[1])
    kuu_sõnadega=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu_sõnadega= kuu_sõnadega[(kuu-1)]
    if int(isikukood[0])>4:
        aastatuhat=20
    elif int(isikukood[0])>=3:
        aastatuhat=19
    elif int(isikukood[0])<3:
        aastatuhat=18
    aasta= str(isikukood[1]+isikukood[2])
    return('{0}. {1} {2}{3}'.format(päev, kuu_sõnadega, aastatuhat, aasta))