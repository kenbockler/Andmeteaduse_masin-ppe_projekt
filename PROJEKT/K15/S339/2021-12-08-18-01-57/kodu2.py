def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min = i
        for j in range(i+1, len(järjend)):
            if järjend[min][1] > järjend[j][1]:
                min = j
            if järjend[min][1] == järjend[j][1]:
                if järjend[min][0] > järjend[j][0]:
                    min = j
        järjend[min], järjend[i] = järjend[i], järjend[min]       