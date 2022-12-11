def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        for i in range(len(järjend)):
            for j in range(len(järjend)-i-1):
                if järjend[j][0]>järjend[j+1][0]:
                    järjend[j], järjend[j+1]=järjend[j+1], järjend[j]
        for i in range(len(järjend)):
            for j in range(len(järjend)-i-1):
                if järjend[j][1]>järjend[j+1][1]:
                    järjend[j], järjend[j+1]=järjend[j+1], järjend[j]
järjesta_punktid([(3, 6), (5, 3), (2, 2), (2, 1), (3, 5), (4, 6)])