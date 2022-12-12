def rek_abs(a):
    absoluutväärtus=[]
    for i in range(len(a)):
        if isinstance(a[i], list):
            absoluutväärtus+=[rek_abs(a[i])]
        elif isinstance(a[i], list)==False:
            absoluutväärtus+=[abs(a[i])]
    return absoluutväärtus
            