isikukood=''
def s�nnikuup�ev(isikukood):
    isikukood=list(isikukood)
    aasta_algus=''
    if isikukood[0]=='1' or isikukood[0]=='2':
        aasta_algus='18'
    elif isikukood[0]=='3' or isikukood[0]=='4':
        aasta_algus='19'
    elif isikukood[0]=='5' or isikukood[0]=='6':
        aasta_algus='20'
    aasta=isikukood[1:3]
    aasta=''.join(aasta)
    aasta=''.join([aasta_algus,aasta])
    kuu=isikukood[3:5]
    kuu=''.join(kuu)
    if kuu=='01':
        kuu='jaanuar'
    elif kuu=='02':
        kuu='veebruar'
    elif kuu=='03':
        kuu='m�rts'
    elif kuu=='04':
        kuu='aprill'
    elif kuu=='05':
        kuu='mai'
    elif kuu=='06':
        kuu='juuni'
    elif kuu=='07':
        kuu='juuli'
    elif kuu=='08':
        kuu='august'
    elif kuu=='09':
        kuu='september'
    elif kuu=='10':
        kuu='oktoober'
    elif kuu=='11':
        kuu='november'
    elif kuu=='12':
        kuu='detsember'
    kuup�ev=isikukood[5:7]
    kuup�ev=''.join(kuup�ev)
    kuup�ev=kuup�ev+'.'
    s�nniaeg=' '.join([kuup�ev,kuu,aasta])
    return s�nniaeg
print(s�nnikuup�ev('39910122345'))
    