def moos(a,b,c):
    kasutatud = 0
    while c >= 5 and a > 0:
        c -= 5
        kasutatud += 1
        a -= 1
    while (a == 0 or c < 5) and c > 0 and b > 0:
        c -= 1
        kasutatud +=1
        b -= 1
    if c != 0:
        kasutatud = int(-1)
    return(kasutatud)
