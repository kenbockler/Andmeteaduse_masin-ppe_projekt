a= int(input(" a "))
b= int(input(" b "))
c= int(input(" c "))
def moos(a,b,c):
    i = 0
    while a > 0 and c >= 5:
        c = c - 5
        a -= 1
        i += 1
    while b > 0 and c >= 1:
        c = c - 1
        b -= 1
        i += 1
    if c > 0 and b <= 0:
        return -1
    else:
        return i
moos(a,b,c)
