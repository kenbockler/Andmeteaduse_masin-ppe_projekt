n = input("Mis on sinu kasutajanimi?")
p1 = input("Mis on kasutajanime parool?")
p2 = input("Korda parooli")
while True:
    if p1 == p2:
        break
    if p1 != p2:
        print("Esimene ja teine parool ei ühti")
    p1 = input("Mis on kasutajanime parool?")
    p2 = input("Korda parooli")
while True:
    if len(p1) >= 8:
        break
    if len(p1) < 8:
        print("Parool on liiga lühike")
    p1 = input("Mis on kasutajanime parool?")
    p2 = input("Korda parooli")
list = []
while True:
    for i in p1:
        y = i.isnumeric()
        s = str(y)
        list.append(s)
    x = len(p1)
    y = list.count("False")
    z = list.count("True")
    if x != y:
        break
    if x == y:
        print("Sisesta parool tähemärkide ja numbritega")
    p1 = input("Mis on kasutajanime parool?")
    p2 = input("Korda parooli")
list2 = []
for i in p1:
    y1 = i
    s1 = str(y1)
    list2.append(s1)
r = list2.reverse()
string= ""
j = string.join(list2)
f = open("users.txt", "w")
f.writelines(str(n))
f.writelines(":")
f.writelines(str(j))
f.close()