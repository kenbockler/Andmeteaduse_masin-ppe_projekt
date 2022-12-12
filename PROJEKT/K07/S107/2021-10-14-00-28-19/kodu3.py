kuud = ("jaanuar","veebruar","märts","aprill","mai","juuni",
           "juuli","august","september","oktoober","november","detsember")
isikukood = input("Sisesta isikukood: ")
def sünnikuupäev(isikukood):
    if isikukood[0] == "1" or isikukood[0] == "2":
        sünniaasta = 1800
    if isikukood[0] == "3" or isikukood[0] == "4":
        sünniaasta = 1900
    if isikukood[0] == "5" or isikukood[0] == "6":
        sünniaasta = 2000
    aastad = int(isikukood[1:3])
    sünniaasta += aastad
    sünnikuu = int(isikukood[3:5])
    sünnipäev = int(isikukood[5:7])
    print(str(sünnipäev)+".",str(kuud[sünnikuu-1]), str(sünniaasta))
sünnikuupäev(isikukood)