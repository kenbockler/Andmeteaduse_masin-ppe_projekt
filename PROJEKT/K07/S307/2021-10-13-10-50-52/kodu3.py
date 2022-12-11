kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november','detsember']
sajandid = ['18', '18','19','19', '20', '20', '21', '21', '22', '22']
def sünnikuupäev(str):
    vastus = ''
    sajandi_indeks = int(str[0])
    sajand = sajandid[sajandi_indeks-1]
    aasta = str[1:3]
    kuupäev = str[5:7]
    kuu_indeks = 0
    if str[3] == '0':
        kuu_indeks = int(str[4])
    elif str[3] == '1':
        kuu_indeks = int(str[3:5])
    kuu = kuud[kuu_indeks -1]
    return vastus + kuupäev + '.' + ' ' + kuu + ' ' + sajand + aasta
