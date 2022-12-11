def sünnikuupäev(isikukood):
    p2ev = 0
    kuu = 0
    aasta = 0
    sugu = 0
    for digit in isikukood:
        x = digit.split(" ")
        sugu = x[0]
        p2ev = x[5, 6]
        kuu = x[3, 4]
        aasta = x[1, 2]
        if sugu(0) == '3' or sugu(0) == '4':
            aasta = str(19) + aasta(1,2)
        if sugu(0) == '5' or sugu(0) == '6':
            aasta = str(20) + aasta (1, 2)
        if kuu (3, 4) == "01":
            kuu = 'jaanuar'
        elif kuu (3, 4) == "02":
            kuu = 'veebruar'
        elif kuu (3, 4) == "03":
            kuu = 'märts'
        elif kuu (3, 4) == "04":
            kuu = 'aprill'
        elif kuu (3, 4) == "05":
            kuu = 'mai'
        elif kuu (3, 4) == "06":
            kuu = 'juuni'
        elif kuu (3, 4) == "07":
            kuu = 'juuli'
        elif kuu (3, 4) == '08':
            kuu = 'august'
        elif kuu (3, 4) == '09':
            kuu = 'september'
        elif kuu (3, 4) == '10':
            kuu = 'oktoober'
        elif kuu (3, 4) == '11':
            kuu = 'november'
        elif kuu (3, 4) == '12':
            kuu = 'detsember'
        p2ev = x(5, 6)
        return(p2ev, kuu, aasta)
sünnikuupäev("50428149923")
print(sünnikuupäev("50428149923"))