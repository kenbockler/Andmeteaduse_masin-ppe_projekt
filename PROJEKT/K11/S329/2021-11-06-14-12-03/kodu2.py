def transponeeriK(m):
    tr_m = []
    a = len(m[0])
    for el in m:
        if a != len(el):
            print("Maatriksit ei transponeerida, kuna elemente pole.")
            return
    for x in range(len(m[0])):
        järjend = []
        for y in m:
           järjend.append(y[-1])
           y.pop()
        järjend.reverse()
        tr_m.append(järjend)
    return(tr_m)