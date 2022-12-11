tulu= float(input('Sisesta oma aastatulu '))
valem= 6000- 6000/ 10800* (tulu - 14400)
if tulu <=0 :
    print('Sisesta positiivne arv!')
else:
    if tulu < 6000 :
        print('Maksuvaba tulu on '+ str(tulu) + ' eurot.')
    elif tulu >= 6000 and tulu < 14400:
        print('Maksuvaba tulu on '+ '6000' + ' eurot.')
    elif tulu >= 14400 and tulu < 25200:
        print('Maksuvaba tulu on '+ str(round(valem, 2)) + ' eurot.')
    elif tulu >= 25200 :
        print('Maksuvaba tulu on '+ '0' + ' eurot.')
'''
automaatkontrollile ei meeldinud minu while tsükkel,
millega ma hoidsin programmi töös, et saaks järjepanu sisendeid kontrollida
kasutaja sai programmist väljuda sisendiga "0". automaatkontroll seda ei osanud
kommenteerisin selle välja, aga ta tegelikult peaks töötama.
'''