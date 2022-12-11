def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min = i
        for l in range(i + 1 , len(järjend)):
            if järjend[min][1] > järjend[l][1]:
                min = l
            if järjend[min][1] == järjend[l][1]:
                if järjend [min][0] > järjend[l][0]:
                    min = l
            järjend[min], järjend[i] = järjend[i], järjend[min]
    return järjend
